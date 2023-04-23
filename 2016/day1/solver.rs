use std::fs;

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let instructions = file.strip_suffix("\n").unwrap().split(", ");
    let mut position: [i32; 2] = [0; 2];
    let mut direction: i32 = 0;
    for item in instructions {
        if item.chars().nth(0).unwrap() == 'R' {
            direction = (direction+1)%4;
        }
        if item.chars().nth(0).unwrap() == 'L' {
            direction = (direction+3)%4;
        }
        let num: String = item.chars().skip(1).collect();
        let i: i32 = num.parse().unwrap();
        if direction == 0 {
            position[0] += i;
        }
        if direction == 1 {
            position[1] += i;
        }
        if direction == 2 {
            position[0] -= i;
        }
        if direction == 3 {
            position[1] -= i;
        }
    }
    let res: i32 = position[0].abs() + position[1].abs();
    println!("{:?}", res);
}

