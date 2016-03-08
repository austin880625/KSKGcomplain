jQuery.noConflict();
jQuery(document).ready(function(){
    jQuery("#submit_button").click(function(){
        var cont=jQuery("#editor").val();
        if(cont.replace(/(\r\n|\n|\r)/gm,"").length<10)
        {
            jQuery("#submit_button").text("內文未滿十個字！");
        }
        else
        {
            jQuery("#id_submission_context").text(cont);
            jQuery("#submission_form").submit();
        }
    });
});

function cont_change()
{
    var cont=document.getElementById("editor").value;
    if(cont.length>=10)
    {
        jQuery("#submit_button").text("Submit");
    }
}
