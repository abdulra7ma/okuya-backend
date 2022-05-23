//              LIKE-BACK
let like = document.getElementById('comment-like')
let likeBack = false;

like.onclick = function (){
    likeBack = !likeBack
    if (likeBack){
        this.style.color = '#4070f4';
    }
    else {
        this.style.color = '';
    }
    return false
};