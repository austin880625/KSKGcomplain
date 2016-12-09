var xhttp = new XMLHttpRequest();
function edit_submission(sub_id)
{
    $("#edit_submission_id").val(sub_id);
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            document.getElementById("editor").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET","/manage/fetch_submission/?id="+sub_id.toString(),true);
    xhttp.send();
    $(".edit_window").show();
}
$(document).ready(function(){
    $("#publish_button").click(function(){
        $("#form_op_type").val("publish");
        $("#publish_form").submit();
    });
    $("#delete_button").click(function(){
        $("#form_op_type").val("delete");
        $("#publish_form").submit();
    });
    $("#cancel_button").click(function(){
        document.getElementById("editor").innerHTML="";
        $(".edit_window").hide();
    });
    $("#save_button").click(function(){
        var new_cont=document.getElementById("editor").value;
        var sub_id=$("input[name=submission_id]").val();
        var csrf=$("input[name=csrfmiddlewaretoken]").val();
        $.post("/manage/update_submission/",{
            "context": new_cont,
            "id": sub_id,
            "csrfmiddlewaretoken": csrf
        });
        xhttp.onreadystatechange = function() {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                document.getElementById("sub_cont_"+sub_id.toString()).innerHTML=xhttp.responseText.replace("\n","<br />").replace("\r\n","<br />");
            }
        };
        xhttp.open("GET","/manage/fetch_submission/?id="+sub_id.toString(),true);
        xhttp.send();
        document.getElementById("editor").innerHTML="";
        $(".edit_window").hide();
    });
});
