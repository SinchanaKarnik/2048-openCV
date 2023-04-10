
var board;
var score = 0;
var rows = 4;
var columns = 4;

window.onload = function() {
    setGame();
}

function setGame() {
    board = [
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]
    ]

    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < columns; c++){
            let tile = document.createElement("div");
            tile.id = r.toString() + '-' + c.toString();
            let num = board[r][c]
            updateTile(tile, num);
            document.getElementById("board").append(tile)
        }
    }
    setTwoAndFour();
    setTwoAndFour();
}

function hasEmptyTile(){
    for (let r=0; r < rows; r++){
        for(let c = 0; c < columns; c++) {
            if (board[r][c] == 0){
                return true;
            }
        }
    }
    return false
}


function setTwoAndFour() {
    if (!hasEmptyTile()){
        finalscore = document.getElementById('score').innerText
        window.location.href="GameOver.html?finalscore=" + finalscore;
        document.getElementById("finalscore").innerHTML = finalscore;
        return;
    }
    let found = false;
    while(!found) {
        let r = Math.floor(Math.random() * rows);
        let c = Math.floor(Math.random() * columns);

        do {
        ran_num = Math.floor(Math.random()*4 + 1)
        } while (ran_num % 2 == 1)

        if (board[r][c]==0){
            board[r][c] = ran_num;
            let tile = document.getElementById( r.toString() + "-" + c.toString());
            tile.innerText = ran_num.toString();
            tile.classList.add("tile" + ran_num.toString());
            found=true;

        }
    }
}

function updateTile(tile, num) {
    tile.innerText = "";
    tile.classList.value = "";
    tile.classList.add("tile");

    if (num > 0) {
        tile.innerText = num.toString();
        if (num <= 4096){
            tile.classList.add("tile" + num.toString())
        } else {
            tile.classList.add("tile8192")
        }
    }
}

document.addEventListener("keyup",(e) =>{
    console.log(e)
    if (e.code == 'ArrowLeft'){
        slideLeft();
        setTwoAndFour();
    }
    else if (e.code == 'ArrowRight'){
        slideRight();
        setTwoAndFour();
    }
    else if (e.code == 'ArrowUp'){
        slideUp();
        setTwoAndFour();
    }
    else if (e.code == 'ArrowDown'){
        slideDown();
        setTwoAndFour();
    }
    document.getElementById("score").innerText = score;
} )

function filterZero(row) {
    return row.filter(num => num!=0);
}

function slide(row){
 row = filterZero(row)
  for (let i = 0; i < row.length -1; i ++){
    if (row[i] == row[i+1]){
        row[i] *= 2;
        row[i+1] = 0;
        score += row[i];
    }
  }

  row = filterZero(row);
  while(row.length < columns){
    row.push(0)
  }
  return row;
}

function slideLeft() {
    for (let r = 0; r < rows; r++){
        let row = board[r];
        row = slide(row);
        board[r] = row;

        for (let c=0; c < columns; c++){
            let tile = document.getElementById(r.toString() + "-" + c.toString());
            let num = board[r][c];
            updateTile(tile, num);
        }
    }
}

function slideRight() {
    for (let r = 0; r < rows; r++){
        let row = board[r];
        row.reverse();
        row = slide(row);
        row.reverse();
        board[r] = row;

        for (let c=0; c < columns; c++){
            let tile = document.getElementById(r.toString() + "-" + c.toString());
            let num = board[r][c];
            updateTile(tile, num);
        }
    }
}

function slideUp() {
    for (let c=0; c < columns; c++){
        let row = [board[0][c], board[1][c], board[2][c], board[3][c]];
        row = slide(row)
        //board[0][c] = row[0];
        //board[1][c] = row[1];
        //board[2][c] = row[2]
        //board[3][c] = row[3];
    
        for (let r=0; r < rows; r++){
            board[r][c] = row[r];
            let tile = document.getElementById(r.toString() + "-" + c.toString());
            let num = board[r][c];
            updateTile(tile, num);
        }
    }
}

function slideDown() {
    for (let c=0; c < columns; c++){
        let row = [board[0][c], board[1][c], board[2][c], board[3][c]];
        row.reverse()
        row = slide(row)
        row.reverse()
        //board[0][c] = row[0];
        //board[1][c] = row[1];
        //board[2][c] = row[2]
        //board[3][c] = row[3];
    
        for (let r=0; r < rows; r++){
            board[r][c] = row[r];
            let tile = document.getElementById(r.toString() + "-" + c.toString());
            let num = board[r][c];
            updateTile(tile, num);
        }
    }
}


