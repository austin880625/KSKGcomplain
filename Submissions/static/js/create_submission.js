var is_animating=-1;
var iid=-1;
var body = document.body,
    html = document.documentElement;
var width = Math.max( html.clientWidth, html.scrollWidth, html.offsetWidth );
var height=Math.max( html.clientHeight, html.scrollHeight, html.offsetHeight )
var images=[];
var posx=[],posy=[];

function frame(){
    if(is_animating==-1){
        jQuery("#animate_layer").hide();
        clearInterval(iid);
        iid=-1;
        for(var i=0;i<images.length;i++){
            posy[i]=-20;
        }
    }
    else{
        for(var i=0;i<images.length;i++){
            //posx[i]+=Math.random() < 0.5 ? -1 : 1;
            posy[i]+=Math.floor(Math.random()*3+1);
            images[i].style.top=posy[i]+'px';
            images[i].style.left=posx[i]+'px';
            if(posy[i]>height){posy[i]=-20;posx[i]=Math.floor(Math.random()*width);}
        }
    }
}

function start_animation(){
    for(var i=0;i<25;i++){
        images.push(document.createElement('img'));
        images[i].setAttribute('class','little_image');
        images[i].setAttribute('src', 'https://dl.dropboxusercontent.com/u/23825208/snow.svg');
        posy.push(Math.floor(Math.random()*height));
        posx.push(Math.floor(Math.random()*width));
        images[i].style.top=posy[i];
        images[i].style.left=posx[i]
        document.getElementById("animate_layer").appendChild(images[i]);
    }
    is_animating=1;
    jQuery("#animate_layer").show();
    if(iid==-1)iid=setInterval(frame,50);
}

jQuery.noConflict();
jQuery(document).ready(function(){
    var css="background-color:#000; font-size: 48px; color: #F00;";
    console.log("%c%s",css,"你他康普爛的在看殺小？");
    css="background-color:#000; font-size: 48px; color: #000;";
    console.log("%c%s",css,"幹你連反白的都看(╯‵□′)╯︵┴─┴");
    start_animation();

    jQuery("#submit_button").click(function(){
        var cont=jQuery("#editor").val();
        if(cont.replace(/(\r\n|\n|\r)/gm,"").length<10)
        {
            jQuery("#submit_button").text("內文未滿十個字！");
        }
        else
        {
            jQuery("#submission_form").submit();
        }
    });
});

function cont_change()
{
    var cont=document.getElementById("editor").value.replace(/(\r\n|\n|\r)/gm,"");
    if(cont.length>=10)
    {
        jQuery("#submit_button").text("Complain!");
    }
    else {
        jQuery("#submit_button").text("內文未滿十個字！");
    }
}
