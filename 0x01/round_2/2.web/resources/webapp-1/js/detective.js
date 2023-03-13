window.onload = function(){  
    var flagged = false;

    document.getElementById("bear-img").onmousedown = function () {
        flagged = !flagged;

        /* Here's a little bit more:
         * _commentary_on_
         */

        if ( flagged ) {
            document.getElementById("flag-text").innerText = "sick flag{lol_nope} bruh";
        } else {
            document.getElementById("flag-text").innerText = "sick flag{} bruh";
        }
    };
}
