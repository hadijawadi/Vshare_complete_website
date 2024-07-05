


// these codes are for likeing and disliking the user post 

let like_btn = document.getElementById("like_btn");
let dislike_btn = document.getElementById("dislike_btn");


like_btn.addEventListener('click',()=>{
    like_btn.textContent= 'you Liked';
    if(dislike_btn.textContent == 'you disliked'){
        dislike_btn.textContent= 'dislike';
    }


});
dislike_btn.addEventListener('click',()=>{
    dislike_btn.textContent= 'you disliked';
    if(like_btn.textContent == 'you Liked'){
        like_btn.textContent= 'like';
    }

});
