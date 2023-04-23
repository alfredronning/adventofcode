use std::fs;
use std::collections::HashSet;

struct Point {
    x: i32,
    y: i32,
}


fn first_visit_twice(instructions: Vec<&str>) -> i32 {
    let mut position: Point = Point{x:0, y:0};
    let mut direction: i32 = 0;
    let mut visited: HashSet<String> = HashSet::new();
    for item in instructions {
        if item.chars().nth(0).unwrap() == 'R' {
            direction = (direction+1)%4;
        }
        if item.chars().nth(0).unwrap() == 'L' {
            direction = (direction+3)%4;
        }
        let num: String = item.chars().skip(1).collect();
        let i: i32 = num.parse().unwrap();
        for _ in 0..i {
            if direction == 0 {
                position.x += 1;
            }
            if direction == 1 {
                position.y += 1;
            }
            if direction == 2 {
                position.x -= 1;
            }
            if direction == 3 {
                position.y -= 1;
            }
            let string_pos: String = format!("{}{}", position.x, position.y);
            if visited.contains(&string_pos) {
                return position.x.abs() + position.y.abs();
            }
            visited.insert(string_pos);

        }
    }
    return -1;
}

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let instructions = file.strip_suffix("\n").unwrap().split(", ").collect();
    let res = first_visit_twice(instructions);
    println!("{:?}", res);
}

