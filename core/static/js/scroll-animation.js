window.addEventListener('wheel', scroll);

var texto_1 = document.getElementById("text_1");
var texto_2 = document.getElementById("text_2");
var texto_3 = document.getElementById("text_3");
var texto_4 = document.getElementById("text_4");
var texto_5 = document.getElementById("text_5");
var texto_6 = document.getElementById("text_6");

var title = document.getElementById("title-id");

var logo = document.getElementById("logo");

$(title).css({'top': 350});

let elements = [
    [texto_1, logo],
    [texto_2, logo],
    [texto_3, logo],
    [texto_4, logo],
    [texto_5, logo],
    [texto_6, logo],
];

for (let group of elements){
     for (let index of group){
        $(index).css({'opacity': 0});
    } 
};

var position = 0;
let transition_delay = 1000;
var scrollDisabled = false;
let counter = 0;

function scroll (e){
    
    if (counter == 0){
        $(title).animate({
            'top': 50,
        }, 500);
        counter = counter + 1;
    }

    if (scrollDisabled){
        return;
    }

    if (position == 0 || position == -1){
        scrollFirstStep(e);
    } else if (position == elements.length){
        console.log("enter")
        scrollLastStep(e);
    } else {
        scrollStep(e);
    }

    scrollDisabled = true
    setTimeout(function(){scrollDisabled = false;}, 800);
}

function scrollFirstStep (e){
    if (position == -1){
            
        for (let content in elements[position]){
            $(elements[position][content]).animate({
                'opacity': 0,
            }, transition_delay);
        }

        position = 0;

    }else{
        if (Math.sign(e.deltaY) == -1){

            for (let content in elements[position]){
                $(elements[position][content]).animate({
                    'opacity': 1,
                }, transition_delay);
            }
    
            for (let content in elements[position]){
                $(elements[position+1][content]).animate({
                    'opacity': 0,
                }, transition_delay);
            }
            position = position + 1;
        }
    }
}

function scrollStep(e){

    if (Math.sign(e.deltaY) == -1){

        for (let content in elements[position]){
            $(elements[position-1][content]).animate({
                'opacity': 0,
            }, transition_delay);
        }

        for (let content in elements[position]){
            $(elements[position][content]).animate({
                'opacity': 1,
            }, transition_delay);
        }

        for (let content in elements[position]){
            try {
                let hide_next = elements[position+1][content];
                $(hide_next).animate({
                    'opacity': 0,
                }, transition_delay);
            } catch (error){

            }
        }

        position = position + 1;

    } else {

        for (let content in elements[position]){
            $(elements[position-1][content]).animate({
                'opacity': 0,
            }, transition_delay);
        }

        for (let content in elements[position]){
            $(elements[position][content]).animate({
                'opacity': 0,
            }, transition_delay);
        }

        for (let content in elements[position]){
            try {
                let hide_next = elements[position-2][content];
                $(hide_next).animate({
                    'opacity': 1,
                }, transition_delay);
            } catch (error){

            }
        }

        position = position - 1;
    }
    console.log("final: " + position)
}

function scrollLastStep(e){
    if (Math.sign(e.deltaY) == 1){
        console.log("here")
        for (let content in elements[elements.length-1]){
            $(elements[position-1][content]).animate({
                'opacity': 0,
            }, transition_delay);
        }

        for (let content in elements[elements.length-2]){
            try {
                let hide_next = elements[position-2][content];
                $(hide_next).animate({
                    'opacity': 1,
                }, transition_delay);
            } catch (error){

            }
        }
        position = position - 1;
    }

}