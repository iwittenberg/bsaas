#[macro_use]
extern crate rocket;

#[get("/")]
fn index() -> String {
    shrug(1)
}

#[get("/<length>")]
fn shrug(length: usize) -> String {
    let lines: Vec<String> = (1..=length)
        .map(|i: usize| {
            let left_spaces = if i == 1 { 0 } else { i };
            let left_body = if i == 1 { r#"¯\"# } else { r#"\"# };
            let left = format!("{}{}", " ".repeat(left_spaces), left_body);

            let middle_spaces = if i == length { 0 } else { 6 + (length - i) * 2 };
            let middle = if i == length {
                r#"_(ツ)_"#.to_owned()
            } else {
                " ".repeat(middle_spaces)
            };

            let right = if i == 1 { r#"/¯"# } else { r#"/"# };

            format!("{}{}{}", left, middle, right)
        })
        .collect();
    lines.join("\n")
}

#[shuttle_runtime::main]
async fn rocket() -> shuttle_rocket::ShuttleRocket {
    let rocket = rocket::build().mount("/", routes![index, shrug]);

    Ok(rocket.into())
}
