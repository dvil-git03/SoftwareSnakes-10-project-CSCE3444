// adds squares to the walls

function add_squares(wall_type){
    const element = document.querySelector('.room_container');
    const grid_size = window.getComputedStyle(element).getPropertyValue('--grid_size') ** 2;
    
    let squares_on_wall = "";
    for(let i=0; i<grid_size; i++){
        squares_on_wall += `<div class="square" id="${i}, ${wall_type}"></div>`;
    }
    document.querySelector(`.room_wall.${wall_type}`).innerHTML = squares_on_wall;
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

tab_container.addEventListener("click", (event) => {
    for(let i = 0; i<item_tabs.length; i++){
        item_tabs[i].style.display = "none";
        if(item_tabs[i].id == event.target.id){
            item_tabs[i].style.display = "grid";
        }
    }
});

// having the selected wallpaper change the color of the walls 
// (will need to update into selecting a specific wall but that will get sorted after i figure out how to get items to go to the specific grid)
let selected_item = "";
let selected_item_type = "";
let edit_notice = document.getElementsByClassName("room_edit_notice")[0];
const element = document.querySelector('.room_container');
const grid_size = window.getComputedStyle(element).getPropertyValue('--grid_size') ** 2;
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

// console.log(room_container);

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

            room_storage[wall_id] = wallpaper_str;
            console.log(room_storage)
        }
        if(selected_item_type == "Items"){
            const tile_id = event.target.id;
            console.log(document.getElementById(tile_id));
            let tile = document.getElementById(tile_id);
            const item_str = `url("images/room_editing/items/${selected_item}")`;
            tile.style.background = "";
            tile.style.backgroundImage = item_str;
            tile.style.backgroundSize = "cover";   // or contain
            tile.style.backgroundRepeat = "no-repeat";
            tile.style.backgroundPosition = "center";
            
            const tile_num = tile_id.split(", ")[0];
            const wall_id = tile_id.split(", ")[1];
            room_storage[wall_id][tile_num] = item_str;
            console.log(room_storage)
            console.log(room_storage[wall_id][tile_num])
        }

        selected_item = "";
        selected_item_type = "";
        edit_notice.style.visibility = "hidden";
    }
});
// alert("this got loaded and actually ran, wow");

