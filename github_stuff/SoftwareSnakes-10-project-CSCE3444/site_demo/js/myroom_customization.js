// adds squares to the walls

function add_squares(wall_type){
    const element = document.querySelector('.room_container');
    const grid_size = window.getComputedStyle(element).getPropertyValue('--grid_size') ** 2;
    
    let squares_on_wall = "";
    for(let i=0; i<grid_size; i++){
        squares_on_wall += `<div class="square" id="${i}, ${wall_type}", item_held=""></div>`;
    }
    document.querySelector(`.room_wall.${wall_type}`).innerHTML = squares_on_wall;
    document.querySelector(`.room_wall.${wall_type}`).style.background = `url("images/room_editing/wallpapers/white_plain.jpeg")`;
    document.querySelector(`.room_wall.${wall_type}`).wallpaper = "images/room_editing/wallpapers/white_plain.jpeg";
}

add_squares("left_wall")
add_squares("right_wall")
add_squares("floor")





// makes the tab menu actually swap between tabs
const tab_container = document.getElementsByClassName("tab_container")[0];
// console.log(tab_container)

let item_tabs = document.getElementsByClassName("item_list")
item_tabs[0].style.display = "grid";
// console.log(item_tabs)


current_tab = "Wallpaper/Flooring"
// event listener for switching tabs
tab_container.addEventListener("click", (event) => {
    for(let i = 0; i<item_tabs.length; i++){
        item_tabs[i].style.display = "none";
        if(item_tabs[i].id == event.target.id){
            item_tabs[i].style.display = "grid";
            current_tab = event.target.id
        }
    }
    edit_menu.style.visibility = "hidden";

});

// having the selected wallpaper change the color of the walls 
// (will need to update into selecting a specific wall but that will get sorted after i figure out how to get items to go to the specific grid)
let selected_item = "";
let selected_item_type = "";
let edit_notice = document.getElementsByClassName("room_edit_notice")[0];
let edit_menu = document.getElementsByClassName("edit_menu")[0];
const element = document.querySelector('.room_container');
const grid_size = window.getComputedStyle(element).getPropertyValue('--grid_size') ** 2;
// let tile_info = {
    //     item_stored : "",
    //     item_rotation : 0
    // }
class tile_info {
    constructor(){
        let item_stored = "";
        let item_rotation = 0;
    }
    set_item_stored(item_to_store){
        this.item_stored = item_to_store;
    }
    set_item_rotation(item_to_rotate){
        this.item_rotation = item_to_rotate;
    }
}
let room_storage = {
    left_wall : {
        background_image : "",
        tiles : new Array(grid_size)
    },
    right_wall : {
        background_image : "",
        tiles : new Array(grid_size)
    },
    floor : {
        background_image : "",
        tiles : new Array(grid_size)
    }
}

for (let i = 0; i < grid_size; i++) {
    room_storage["left_wall"]["tiles"][i] = new tile_info();
    room_storage["right_wall"]["tiles"][i] = new tile_info();
    room_storage["floor"]["tiles"][i] = new tile_info();
}
// room_storage["left_wall"]["tiles"][3].set_item_stored("boom");
console.log(room_storage);

// class room_storage_class {
//     constructor(){
//         let left_wall = new wall_storage();
//         let right_wall = new wall_storage();
//         let floor = new wall_storage();
//     }
// }
// class wall_storage{
//     constructor(){
//         let background_image = "";
//         let tiles = new Array(grid_size).fill(new tile_info());
//     }
// }

// let room_storage = new room_storage_class();

const item_container = document.getElementsByClassName("side_menu")[0];

item_container.addEventListener("click", (event) => {
    // only do something if an image is clicked
    if (event.target.tagName === "IMG") {
        console.log("Clicked:", event.target.id);
        // do whatever you want with the clicked item here
        selected_item = event.target.id;
        selected_item_type = event.target.closest(".item_list").id;
        // console.log(parent_tab);
        if(selected_item_type == "Wallpaper/Flooring"){
            edit_notice.textContent = "⚠️ Notice: Please Select a wall or floor to apply the wallpaper to ⚠️";
        }
        if(selected_item_type == "Items"){
            edit_notice.textContent = "⚠️ Notice: Please Select a tile to place your item ⚠️";
        }
        edit_notice.style.visibility = "visible";
    }
});

// add an event listener to the room_container so then i can check when a specific square gets clicked
const room_container = document.getElementsByClassName("room_container")[0];
// let selected_wall = "";
// let wall_wallpaper = "";
let item_location = "";
let item_square = "";

let tile_num = "";
let wall_id = "";

// console.log(room_container);
// event listener for when a tile is clicked 
room_container.addEventListener("click", (event) => {
    if(event.target.classList.contains("square")){
        console.log("Clicked:", event.target.id);
        console.log(selected_item);
        console.log(selected_item_type);
        
        if(selected_item_type == "Wallpaper/Flooring"){
            const wall_id = event.target.id.split(", ")[1];
            let selected_wall = document.getElementsByClassName(wall_id)[0];
            // console.log(selected_item)
            const wallpaper_str = `url("images/room_editing/wallpapers/${selected_item}")`;
            // console.log(wallpaper_str)
            selected_wall.style.background = "";
            selected_wall.style.backgroundImage = wallpaper_str;
            selected_wall.wallpaper = wallpaper_str.replace("url(\"", "").replace("\")", "");
            
            room_storage[wall_id]["background_image"] = wallpaper_str;
            console.log(room_storage)
        }
        else if(selected_item_type == "Items"){
            const tile_id = event.target.id;
            console.log(document.getElementById(tile_id));
            let tile = document.getElementById(tile_id);
            const item_str = `url("images/room_editing/items/${selected_item}")`;
            tile.style.background = "";
            tile.style.backgroundImage = item_str;
            tile.style.backgroundSize = "cover";   // or contain
            tile.style.backgroundRepeat = "no-repeat";
            tile.style.backgroundPosition = "center";
            tile.item_held = `images/room_editing/items/${selected_item}`;
            
            // tile.style.rotate = '90deg';
            
            tile_num = tile_id.split(", ")[0];
            wall_id = tile_id.split(", ")[1];
            room_storage[wall_id]["tiles"][tile_num].set_item_stored(item_str);
            console.log(room_storage)
            console.log(room_storage[wall_id]["tiles"][tile_num].item_stored)
        }

        selected_item = "";
        selected_item_type = "";
        edit_notice.style.visibility = "hidden";
        
        if(selected_item == ""){
            
            if(current_tab == "Items"){
                console.log("w")
                console.log(current_tab)
                // const wall_id = event.target.id.split(", ")[1];
                // selected_item = document.getElementsByClassName(wall_id)[0];
                // wall_wallpaper = selected_wall.wallpaper
                // console.log(wall_wallpaper)
                item_location = event.target.id;
                console.log(`Location of item selected: ${item_location}`)
                item_square = document.getElementById(item_location);
                item_item = item_square.item_held;
                console.log(item_item)
                // console.log(selected_item)
                // console.log(selected_item_type)
                edit_menu.style.visibility = "visible";
                edit_menu.innerHTML = `<h3>${item_location} selected!</h3>
                    <img id="item_display" object-fit="cover" height="100px" width="100px" src="${item_item}" alt="wallpaper">
                    <div id="rotation_container" vertical-align="middle">
                        <img id="rotate_right" object-fit="cover" height="50px" width="50px" src="images/room_editing/rotate-right-variant.svg" alt="rotate right">
                        Rotate Image
                        <img id="rotate_left" object-fit="cover" height="50px" width="50px" src="images/room_editing/rotate-left-variant.svg" alt="rotate left">
                    </div>
                    
                    `
                // console.log(selected_wall.wallpaper)

            }
            if(current_tab == "Wallpaper/Flooring"){
                console.log(current_tab)
            }

        }

    }
});
// alert("this got loaded and actually ran, wow");


// const rotation_container = document.getElementById("rotation_container");
// console.log(rotation_container)
edit_menu.addEventListener("click", (event) => {
    // console.log("clicked")
    console.log(item_square)
    transformations = Number(item_square.style.transform.replace("rotate(", "").replace("deg)", "")) % 360;
    console.log(transformations)
    if(event.target.id == "rotate_right"){
        console.log("will rotate to the right")
        // item_square.style.transform = "rotate(90deg)"
        item_square.style.transform = `rotate(${transformations+90}deg)`
    }
    if(event.target.id == "rotate_left"){
        console.log("will rotate to the left")
        item_square.style.transform = `rotate(${transformations-90}deg)`
    }
    
    transformations = Number(item_square.style.transform.replace("rotate(", "").replace("deg)", "")) % 360;
    console.log(wall_id)
    console.log(tile_num)
    room_storage[wall_id]["tiles"][tile_num].set_item_rotation(transformations);
    console.log(room_storage)
});