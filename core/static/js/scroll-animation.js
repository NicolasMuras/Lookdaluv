window.addEventListener('wheel', scroll);

let position = 0;
var scrollDisabled = false;
var texto_1 = document.getElementById("text_1");
var texto_2 = document.getElementById("text_2");
var texto_3 = document.getElementById("text_3");

var title = document.getElementById("title-id");

var img = document.getElementById("id-img");
var img_2 = document.getElementById("id-img-2");

$(texto_1).css({'opacity':0});
$(texto_2).css({'opacity':0});
$(texto_3).css({'opacity':0});

$(title).css({'top': 320});

$(img).css({'opacity':0});
$(img).css({'width': 0});
$(img).css({'height': 0});

$(img_2).css({'opacity':0});
$(img_2).css({'width': 0});
$(img_2).css({'height': 0});

function scroll(e){
    if (scrollDisabled){
        return;
    }
        
    if (position == 0 || position == -100){
        
        if (position == -100){
            
            $(texto_1).animate({
                'opacity': 0,
            }, 800);

            $(title).animate({
                'top': 320,
            }, 500);

            $(img_2).animate({
                'opacity': 0,
                'width': 0,
                'height': 0,
            }, 1000);

            position = 0;

        }else{
            if (e.deltaY != 100){

                $(texto_1).animate({
                    'opacity': 1,
                }, 800);

                $(title).animate({
                    'top': 50,
                }, 500);

                $(img_2).animate({
                    'opacity': 0,
                    'width': 200,
                    'height': 200,
                }, 100);
    
                $(img_2).animate({
                    'opacity': 1,
                    'width': 300,
                    'height': 300,
                }, 100);
        
                $(texto_2).animate({
                    'opacity': 0,
                }, 800);
            }
            position = position + (-e.deltaY);
        }

        console.log(position);

    }else if (position == 100){
        
        if (e.deltaY != 100){

            $(texto_1).animate({
                'opacity': 0,
            }, 800);

            $(img_2).animate({
                'opacity': 0,
                'width': 0,
                'height': 0,
            }, 1000);
            
            $(texto_2).animate({
                'opacity': 1,
            }, 800);

        }else{
            $(texto_1).animate({
                'opacity': 0,
            }, 800);

            $(texto_2).animate({
                'opacity': 0,
            }, 800);

            $(title).animate({
                'top': 320,
            }, 500);

            $(img_2).animate({
                'opacity': 0,
                'width': 0,
                'height': 0,
            }, 1000);
        }

        position = position + (-e.deltaY);
        console.log(position);

    }else if (position == 200){

        if (e.deltaY != 100){
            $(texto_1).animate({
                'opacity': 0,
            }, 800);

            $(texto_2).animate({
                'opacity': 1,
            }, 800);

        }else{
            $(texto_1).animate({
                'opacity': 1,
            }, 800);

            $(img_2).animate({
                'opacity': 1,
                'width': 300,
                'height': 300,
            }, 500);

            $(texto_2).animate({
                'opacity': 0,
            }, 800);

            $(texto_3).animate({
                'opacity': 0,
            }, 800);

            $(img).animate({
                'opacity': 0,
                'width': 0,
                'height': 0,
            }, 1000);

        }

        position = position + (-e.deltaY);
    
        console.log(position);

    }else if (position == 300){

        if (e.deltaY != 100){
            $(texto_2).animate({
                'opacity': 0,
            }, 800);
    
            $(img).animate({
                'opacity': 0,
                'width': 300,
                'height': 300,
            }, 100);

            $(img).animate({
                'opacity': 1,
                'width': 400,
                'height': 400,
            }, 100);

            $(texto_3).animate({
                'opacity': 1,
            }, 8000);

        }else{
            $(texto_1).animate({
                'opacity': 0,
            }, 800);

            $(texto_2).animate({
                'opacity': 1,
            }, 800);

            $(texto_3).animate({
                'opacity': 0,
            }, 800);

            $(img).animate({
                'opacity': 0,
                'width': 0,
                'height': 0,
            }, 1000);
        }

        position = position + (-e.deltaY);
    
        if (position == 400){
            position = 300;
        }
        console.log(position);
    }

    
    scrollDisabled = true
    setTimeout(function(){scrollDisabled = false;}, 1000);
}