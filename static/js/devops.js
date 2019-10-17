CheckAll();
ShowSenior();
SearchProcess();
OptionHistory();
ShowRollbackTagProject();
ShowUpdtaeTagProject();
DeleteSelectCheckbox();
ShowAuthServer();
allCheck();
ShowAuthProject();
DeleteUser();
DeleteRoles();
ShowCreateServerUser();
ShowProjectoOnlineNoticeInput();

function CheckAll() {
    $("#check-all").click(function() {
    if (this.checked) {
        $("input[name='items']:checkbox").each(function() { //遍历所有的name为selectFlag的 checkbox
            $(this).attr("checked", true);
                        $(this).prop("checked",true);     //要写这个，否则全选用不了
            })
        } else {   //反之 取消全选
        $("input[name='items']:checkbox").each(function() { //遍历所有的name为selectFlag的 checkbox
            $(this).attr("checked", false);
            $(this).prop("checked",false);     //要写这个，否则全选用不了
        })
    }
})
}

function AddReviewer(img,name,id){
        content = `<div class="form-group">
                        <div  class=" col-md-9 col-sm-9 col-xs-12" id="option_flag_id" >
                        <label class="control-label col-md-3 col-sm-3 col-xs-12">flag_name</label>
                          <img src="/img.jpg" height="100" width="100">
                          <input type="button" value="删除" onclick="DeleteReviewer(this.name);"  flag_n="flag_name"  name="delete_reviewer"  style="display: inline;">
                          <input style="display: none;" type="checkbox" name="flag_id" checked="checked">
                            <p></p>
                     </div>
               </div>
        `
        content1 = content.replace("img.jpg",img)
        content2 = content1.replace(/flag_name/g,name)
        $("[name='username']:last").append(content2.replace(/flag_id/g,id))
        $('#myModal').modal('toggle') //关闭模态框

        span_id = name + "_" + id
        document.getElementById(id).remove();
        document.getElementById(span_id).remove();

}

function DeleteReviewer(obj) {
    id = $('[name='+obj+']').next().attr("name");
    myname = $('[name='+obj+']').attr("flag_n")

    //删除
    option_id = "option_" + id
    img = $("#"+option_id).find('img').attr("src");
    label_content = `
             <img onclick="AddReviewer('{{ i.head_img }}','{{ i.name }}','{{ i.id }}');" id="{{ i.id }}" src="{{ i.head_img }}"  height="80" width="80">
             <span id="{{ i.name }}_{{ i.id }}">{{ i.name }}</span>
    `
    label_content1 = label_content.replace(/{{ i.head_img }}/g,img).replace(/{{ i.name }}/g,myname).replace(/{{ i.id }}/g,id);
    $("#"+option_id).remove();
    $('.reviewer_list').append(label_content1);

}

function ChangePageForm() {
    var form = document.getElementById("change_page_form");
    form.submit();

}
function DeletePorcessId(id,name) {
    $('#delete_process_content').text("删除"+name+" ?");
    $('#delete_process_button').attr('remove_process_id',id);

}

function DeletePorcess(id) {
    user_id = $('#'+id).attr('remove_process_id');
    $.ajax({
            url: '/process/delete/',
            type: "POST",
            data: {'id':user_id},
            dataType: "json",
            success: function () {
                window.location.reload();
            }
        });
}

function DeleteSelectCheckbox() {
    $('#delete_process_all').click(function () {
        var checkID = [];
        $("input[name='items']:checked").each(function(i){//把所有被选中的复选框的值存入数组
            checkID[i] =$(this).attr('id');
        });
        $.ajax({
            url: '/process/delete/',
            type: "POST",
            data: {'del_id_lsit':checkID},
            dataType: "json",
            success: function () {
                window.location.reload();
            }
        });
    })

}

function SearchProcess() {
    $('#search_process_button').click(function () {
        v = $('.search_process').val();
        $.get('/process/list/?search=',v,);

    })

}


$(function () {
        $('.tab-menu li').click(function () {
            $(this).addClass('active').siblings().removeClass('active');
            var index=$(this).index();
            $(".tab-con div").eq(index).show().siblings().hide();
        })
})


function OptionHistory() {
    $('#dispaly_option_process_select').change(function () {
        var form = document.getElementById("option_history_form");
        form.submit();
    })
    
}

$("#img_input").on("change", function(e){
  var file = e.target.files[0]; //获取图片资源
  // 只选择图片文件
  if (!file.type.match('image.*')) {
    return false;
  }
  var reader = new FileReader();
  reader.readAsDataURL(file); // 读取文件
  reader.onload = function(arg) {
    var img = '<img class="preview" src="' + arg.target.result + '" alt="preview"/>';
    $(".preview_box").empty().append(img);
  }
});

function allCheck() {
    $("#checkAll").click(function () {
        if (this.checked) {
            $("input[name='items']:checkbox").each(function () {
                $(this).attr("checked", true);
                $(this).prop("checked", true);
            })
        } else {
            $("input[name='items']:checkbox").each(function () {
                $(this).attr("checked", false);
                $(this).prop("checked", false);
            })
        }
    })
};

function CheckMenu(menu,a) {
    status = $('.'+menu+"_group").attr('status')
    if (status == 'off'){
        $("."+menu).each(function () {
        $(this).attr("checked", true);
        $(this).prop("checked", true);
        $('.'+menu+"_group").attr('status','on');
        })
    }else{
        $("."+menu).each(function () {
        $(this).attr("checked", false);
        $(this).prop("checked", false);
        $('.'+menu+"_group").attr('status','off');
        })
    }
}

function DisableUser(nid) {
    $.ajax({
        url: '/permissions/disable/user/',
        type: 'POST',
        data: {'id':nid},
        dataType: "text",
        success: function () {
        }
    })
}



function DeleteUserContent(id,name) {
    $('#delete_user').text(name);
    $('#delete_user_button').attr('delete_user_id',id)
}


function DeleteUser() {
    $('#delete_user_button').click(function () {
        user_id = $('#delete_user_button').attr('delete_user_id');
        $.ajax({
                url: '/permissions/delete/user/',
                type: "POST",
                data: {'user_id':user_id},
                dataType: "text",
                success: function () {
                    window.location.reload();
                }
            });
    })
}


function DeleteRolesContent(id,name) {
    $('#delete_roles').text(name);
    $('#delete_roles_button').attr('delete_roles_id',id)
}


function DeleteRoles() {
    $('#delete_roles_button').click(function () {
        role_id = $('#delete_roles_button').attr('delete_roles_id');
        $.ajax({
                url: '/permissions/delete/roles/',
                type: "POST",
                data: {'role_id':role_id},
                dataType: "text",
                success: function () {
                    window.location.reload();
                }
            });
    })
}

function ShowAuthServer() {
    $('input[type=radio][name=ssh_auth]').change(function () {
        if (this.value == 'auth_success') {
            $('#server_auth_id').addClass("server_auth");
        }
        else if (this.value == 'auth') {
            $('#server_auth_id').removeClass("server_auth");
        }
    })
}
function DeleteOperationalContent(id,name) {
    $('#operational_content').text('删除  '+name+'?');
    $('#delete_operational_button').attr('delete_operational_id',id)
}

function DeleteOperational() {
        server_id = $('#delete_operational_button').attr('delete_operational_id');
        $.ajax({
                url: '/operational/delete/server/',
                type: "POST",
                data: {'server_id':server_id},
                dataType: "text",
                success: function () {
                    window.location.reload();
                }
            });
}
function DeleteServerGroupContent(id,name) {
    $('#server_group_content').text('删除  '+name+'?');
    $('#delete_server_group_button').attr('delete_server_group_id',id)
}

function DeleteServerGroup() {
        group_id = $('#delete_server_group_button').attr('delete_server_group_id');
        $.ajax({
                url: '/operational/delete/group/',
                type: "POST",
                data: {'group_id':group_id},
                dataType: "text",
                success: function () {
                    window.location.reload();
                }
            });
}



  $(function(){
	$("#sel_left,#sel_right").bind("change",checkBtn);
	$("#btn_1,#btn_2,#btn_3,#btn_4").bind("click",clickBtn);
	checkBtn();
	});

	function checkBtn(){
		jQuery("#sel_left>option").length > 0 ? jQuery("#btn_1").removeAttr("disabled") : jQuery("#btn_1").attr("disabled","disabled");
		jQuery("#sel_left option:selected").length > 0 ? jQuery("#btn_2").removeAttr("disabled") : jQuery("#btn_2").attr("disabled","disabled");
		jQuery("#sel_right option:selected").length > 0 ? jQuery("#btn_3").removeAttr("disabled") : jQuery("#btn_3").attr("disabled","disabled");
		jQuery("#sel_right>option").length > 0 ? jQuery("#btn_4").removeAttr("disabled") : jQuery("#btn_4").attr("disabled","disabled");
	}

	function clickBtn(e){
		if("btn_1" == e.target.id){
			jQuery("#sel_left>option").appendTo("#sel_right");
		}else if("btn_2" == e.target.id){
			jQuery("#sel_left option:selected").appendTo("#sel_right");
		}else if("btn_3" == e.target.id){
			jQuery("#sel_right option:selected").appendTo("#sel_left");
		}else if("btn_4" == e.target.id){
			jQuery("#sel_right>option").appendTo("#sel_left");
		}
		checkBtn();
	}

	$("#edit_server_group_sub_butten").click(function(){
	var selVal = [];
	$('#sel_right').find("option").each(function(){
		selVal.push(this.value);
	});
    $('#sel_right').val(selVal);
	var form = document.getElementById("edit_server_group_form");
    form.submit();

});

	$("#create_server_butten").click(function(){
	var selVal = [];
	$('#sel_right').find("option").each(function(){
		selVal.push(this.value);
	});
    $('#sel_right').val(selVal);
	var form = document.getElementById("create_server_form");
    form.submit();

});

$("#edit_server_butten").click(function(){
	var selVal = [];
	$('#sel_right').find("option").each(function(){
		selVal.push(this.value);
	});
    $('#sel_right').val(selVal);
	var form = document.getElementById("edit_server_form");
    form.submit();

});

function ShowAuthProject() {
    $('input[type=radio][name=git_auth_way]').change(function () {
        if (this.value == '0') {
            $('#git_user_passwor').removeClass("server_auth");
        }
        else if (this.value == '1') {
            $('#git_user_passwor').addClass("server_auth");

        }
    })
}

function ShowProjectoOnlineNoticeInput() {
    $('#project_online_notice_select').change(function () {
        if (this.value == 'dingding'){
            $('#email_input').addClass("server_auth");
            $('#dingding_input').removeClass("server_auth");
        }
        else if (this.value == 'email'){
            $('#email_input').removeClass("server_auth");
            $('#dingding_input').addClass("server_auth");
        }
    })
}
function DeleteProjectContent(id,name) {
    $('#project_content').text('删除  '+name+'?');
    $('#delete_project_button').attr('delete_project_id',id)
}

function DeleteProject() {
        project_id = $('#delete_project_button').attr('delete_project_id');
        $.ajax({
                url: '/project/delete/',
                type: "POST",
                data: {'project_id':project_id},
                dataType: "text",
                success: function () {
                    window.location.reload();
                }
            });
}




function ShowCreateServerUser() {
    $('input[type=radio][name=way]').change(function () {
        if (this.value == '1') {
            $('#servers').removeClass("server_auth");
            $('#groups').addClass("server_auth");
        }
        else if (this.value == '2') {
            $('#groups').removeClass("server_auth");
            $('#servers').addClass("server_auth");

        }
    })
}


	$("#create_server_user_sub_butten").click(function(){
	var selVal = [];
	$('#sel_right').find("option").each(function(){
		selVal.push(this.value);
	});
    $('#sel_right').val(selVal);
	var form = document.getElementById("create_server_user_form");
    form.submit();

});


	$("#edit_server_user_sub_butten").click(function(){
	var selVal = [];
	$('#sel_right').find("option").each(function(){
		selVal.push(this.value);
	});
    $('#sel_right').val(selVal);
	var form = document.getElementById("edit_server_user_form");
    form.submit();

});



function DeleteServerUserContent(id,name) {
    $('#server_user_content').text('删除 '+'ssh账号 '+name+'?');
    $('#delete_server_user_button').attr('delete_server_user_id',id)
}

function DeleteServerUser() {
        user_id = $('#delete_server_user_button').attr('delete_server_user_id');
        $.ajax({
                url: '/operational/server/delete/user/',
                type: "POST",
                data: {'user_id':user_id},
                dataType: "text",
                success: function () {
                    window.location.reload();
                }
            });
}

function ShowSenior(){
    $('input[type=checkbox][name=senior]').change(function () {
    if (this.checked == true){
        $('#senior').removeClass('server_auth');
    }
    else {
        $('#senior').addClass('server_auth');
    }
    })

}

function SendProjectId(id) {
    $('#update_project_id').attr('value',id);
}

function SendRollbackProjectId(id) {
    $('#rollbac_project_id').attr('value',id);
}


function ShowUpdtaeTagProject() {
    $('input[type=radio][name=update_project_way]').change(function () {
        if (this.value == '0') {
            $('#update_project_tag').addClass("server_auth");
        }
        else if (this.value == '1') {
            update_project_id = $('#update_project_id').val();
            $.ajax({
                    url: '/project/tag/',
                    type: "POST",
                    data: {'update_project_id':update_project_id},
                    dataType: "text",
                    success: function (data) {
                        var tag_list = data.split(",");
                        for (i in tag_list){
                            $('#update_project_tag_select').append("<option value=\'"+tag_list[i]+"\'>"+tag_list[i]+"</option>");
                        }
                        $('#update_project_tag').removeClass("server_auth");

                    }
                })
        }
    })
}

function ShowRollbackTagProject() {

    $('input[type=radio][name=rollbac_project_way]').change(function () {

        if (this.value == '0') {
            $('#rollback_project_tag').addClass("server_auth");
            $('#rollback_project_commit').addClass("server_auth");
        }
        else if  (this.value == '2') {
             $('#rollback_project_commit').removeClass("server_auth");
             $('#rollback_project_tag').addClass("server_auth");

        }
    })
}
function OnFalse(e) {
    $(e).addClass('on_false');
}
