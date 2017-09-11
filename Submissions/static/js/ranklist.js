$(document).ready(function(){
    var ranklist_type=$("#ranklist_type").val();
    $(".nav_bar_item").removeClass("nav_bar_active");
    $("#nav_bar_"+ranklist_type).addClass("nav_bar_active");
    $.ajax({
        type:"GET",
        url:"/ranklist/update",
        data:{ranklist_type:ranklist_type},
        success:function(raw){
            $(".loading").hide();
            var data=JSON.parse(raw);
            for(var i=0;i<Math.min(51,data.length);i++){
                $(".posts").append("<h3>#"+(i+1).toString()+"</h3><div class=\"fb-post single_post\" data-show-text=\"True\" data-href=\""+data[i].permalink_url+"\"></div>");
            }
        }
    });
});
