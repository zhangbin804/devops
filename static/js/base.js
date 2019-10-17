 $(function () {
        bindUpdateUser();
        bindUpdateEmail();
        bindAddCron();
        bindAddRoles();
        bindAddServer();
        bindRemoveServer();
        allCheck();
        bindUpdeRoles();
        bindRemoveRole();
        bindRemoveCron();
        bindAddWww();
        bindRemoveWww();
        bindUserAdd();
        bindUserRemove();
        bindAddSshUser();
        bindRemoveSshUser();
        bindUpdateSshUser();
        bindAddRandomPassword();
        bindNewVersion();
        bindGitVersion();

    });


    function bindAddWww() {
        $('#add_www_submit').click(function () {
            SUBMIT_URL = "/git_code/add_web/"
            var add_www_name = $('#add_www_name').val();
            var add_www_dir = $('#add_www_dir').val();
            if (add_www_name.length == 0 || add_www_dir.length == 0) {
                alert("不能有空值！")

                }
                else {

                $.ajax({
                    url: "/git_code/add_web/",
                    type: "POST",
                    data: {'add_www_name': add_www_name, 'add_www_dir': add_www_dir},
                    dataType: "text",
                    success: function (data) {
                        if(data == 0){
                            alert('已存在相同名的站点，添加失败！')

                        }else {location.reload()}

                    },
                    error: function (data) {
                        alert(data)
                    }

                })}}


        )


    }


    function allCheck() {
    $("#checkAll").click(function() {
    if (this.checked) {
        $("input[name='items']:checkbox").each(function() { //遍历所有的name为selectFlag的 checkbox
            $(this).attr("checked", true);
                        $(this).prop("checked",true);     //要写这个，否则全选用不了
            })
        } else {   //反之 取消全选
        $("input[name='items']:checkbox").each(function() { //遍历所有的name为selectFlag的 checkbox
            $(this).attr("checked", false);
            $(this).prop("checked",false);     //要写这个，否则全选用不了
            //alert("f");
        })
    }
})

    }


    function bindRemoveWww() {
        $('#determine_remove').click(function () {
            var del_web_list=new Array();
            $("input[type='checkbox']:checked").each(function () {
                del_web_list.push($(this).val())


            })
            if(del_web_list.length == 0){
                alert('提交不能为空')
            }else {
                $.ajax({
                    url: '/git_code/delete_web/',
                    type: "POST",
                    data: {'del_web_list':del_web_list},
                    dataType: "text",
                    success: function (data) {
                        location.reload()
                    }

                })

            }

        })
    }


        function bindUserAdd() {
        $('#user_add_submit').click(function () {
            var add_username = $('#add_username').val();
            var add_password = $('#add_password').val();
            var email = $('#add_email').val();
            var add_user = $('#add_user').val();
            var add_role = $('#add_role').val()


            if (add_username.length == 0 || add_password.length == 0) {
                alert("不能有空值！")

                }
                else {

                $.ajax({
                    url: "/user_info/add/",
                    type: "POST",
                    data: {'add_username': add_username, 'add_password': add_password,'email':email,'add_user':add_user,'add_role':add_role },
                    dataType: "text",
                    success: function (data) {
                        if(data == 0 ){
                            alert('添加失败！')
                        }else {
                            location.reload()
                        }
                    },
                    error: function (data) {
                        alert('失败')
                    }

                })}}


        )

    }

    function bindAddServer() {
        $('#add_server_submit').click(function () {
            var add_server = $('#add_server').val();

            if (add_server.length == 0) {
                alert("不能有空值！")

                }
                else {
                $.ajax({
                    url: "/server/add/",
                    type: "POST",
                    data: {'add_server': add_server},
                    dataType: "json",
                    success: function (data) {
                            location.reload()
                    },
                    error: function (data) {
                        alert('失败')
                    }

                })}}

        )

    }


   function bindAddRoles() {
        $('#add_roles_submit').click(function () {
            var add_roles = $('#add_roles_name').val();

            if (add_roles.length == 0) {
                alert("不能有空值！")

                }
                else {
                $.ajax({
                    url: "/permission/add_roles/",
                    type: "POST",
                    data: {'add_roles': add_roles},
                    dataType: "json",
                    success: function (data) {
                            location.reload()
                    },
                    error: function (data) {
                        alert('失败')
                    }

                })}}

        )

    }

    function bindRemoveServer() {
        $('#remove_server').click(function () {
            var del_server_list=new Array();
            $("input[type='checkbox']:checked").each(function () {
                del_server_list.push($(this).val())

            })
            if(del_server_list.length == 0){
                alert('提交不能为空')
            }else {
                $.ajax({
                    url: '/server/delete/',
                    type: "POST",
                    data: {'del_server_list':del_server_list},
                    dataType: "json",
                    success: function (data) {
                        location.reload()
                    },
                    error:function (data) {
                        alert('删除失败')
                    }

                })

            }
        })
    }

        function bindRemoveRole() {
        $('#remove_roles').click(function () {
            var del_roles_list=new Array();
            $("input[type='checkbox']:checked").each(function () {
                del_roles_list.push($(this).val())

            })
            if(del_roles_list.length == 0){
                alert('提交不能为空')
            }else {
                $.ajax({
                    url: '/permission/delete_roles/',
                    type: "POST",
                    data: {'del_roles_list':del_roles_list},
                    dataType: "json",
                    success: function (data) {
                        location.reload()
                    },
                    error:function (data) {
                        alert('删除失败')
                    }

                })

            }
        })
    }

     function bindUpdeRoles() {
        $('#update_roles_permission').click(function () {
            var update_roles_list=new Array();
            var roles_title=$('#roles_title').val();
            $("input[name='items']:checked").each(function () {
                update_roles_list.push($(this).val())


            })
                $.ajax({
                    url: '/permission/edit/update/',
                    type: "POST",
                    data: {'update_roles_list':update_roles_list,'roles':roles_title},
                    dataType: "json",
                    success: function (data) {
                        location.reload()
                    },
                    error:function (data) {
                        alert('删除失败')
                    }

                })


        })
    }


     function bindUserRemove() {
        $('#remove_user_list').click(function () {
            var del_user_list=new Array();
            $("input[type='checkbox']:checked").each(function () {
                del_user_list.push($(this).val())


            })
            if(del_user_list.length == 0){
                alert('提交不能为空')
            }else {

                $.ajax({
                    url: '/user_info/delete/',
                    type: "POST",
                    data: {'del_user_list':del_user_list},
                    dataType: "text",
                    success: function (data) {

                        location.reload()
                    }

                })

            }

        })
    }

    function bindAddSshUser() {
        $('#user_add_ssh_user').click(function () {
            var add_username = $('#add_ssh_username').val();
            var add_password = $('#add_ssh_password').val();
            var add_host = $('#add_server_list').val();

            if (add_username.length == 0 || add_password.length == 0 || add_host.length == 0) {
                alert("不能有空值！")

                }
                else {

                $.ajax({
                    url: "/ssh_user/add/",
                    type: "POST",
                    data: {'add_username': add_username, 'add_password': add_password,'host':add_host },
                    dataType: "json",
                    success: function (data) {
                        location.reload()
                    },
                    error: function (data) {
                        alert('失败')
                    }

                })}}


        )


    }



    function bindRemoveSshUser() {
        $('#remove_ssh_user').click(function () {
            var del_user_list=new Array();
            $("input[type='checkbox']:checked").each(function () {
                del_user_list.push($(this).val())


            })
            if(del_user_list.length == 0){
                alert('提交不能为空')
            }else {

                $.ajax({
                    url: '/ssh_user/delete/',
                    type: "POST",
                    data: {'del_user_list':del_user_list},
                    dataType: "text",
                    success: function (data) {
                        location.reload()
                    },
                    error: function (data) {
                        alert('失败')
                    }

                })

            }

        })
    }

     function bindUpdateSshUser() {

        $('#update_ssh_user_password').click(function () {
            var update_password = $("#update_ssh_password").val();
            var username = document.getElementById("username").innerHTML;
            if(update_password.length == 0){
                alert('提交不能为空')

            }else {
                 $.ajax({
                url: '/update_ssh_password_user',
                type: 'POST',
                data: {'password':update_password,'username':username},
                dataType: 'json',
                success:function () {
                    alert('ssh密码修改成功');
                    location.reload()
                    },
                error:function () {
                    alert('修改失败')

                }

            })

            }

        })

    }

    function bindNewVersion() {
        var www_name=document.getElementById("git_www_name").innerText;
        $('#new_version').click(function () {
             $('#new_version').attr("disabled",'disabled');
            $.ajax({
                url: '/git_code/update_new_www/',
                type: 'POST',
                data: {'www_name':www_name},
                dataType:'json',
                success:function (data) {
                        location.reload()
                    },
                error:function () {
                    alert('更新失败')
                }

            })

        })

    }

    function bindGitVersion() {
        $('#determine').click(function () {
            var commit_id=$('#history_version').val();
            var comment=$('#history_version').find("option:selected").text();
            var www_name=document.getElementById("git_www_name").innerText;
            $('#determine').attr("disabled",'disabled');
            $.ajax({
                url: "/git_code/version_retreat/",
                type: 'POST',
                data: {'commit_id':commit_id,'comment':comment,'www_name':www_name},
                dataType:'text',
                success:function (data) {
                        location.reload()
                    },
                error:function () {
                    alert('回滚失败')
                }

            })


        })

    }

     function bindUpdateUser() {

        $('#svae_user_info').click(function () {
            var update_password = $("#update_password").val();
            var update_email = $("#update_email").val();
            var user = $("#_user").val();
            var username = $("#update_username").val();
            var update_roles = $("#update_roles option:selected").val();

            $.ajax({
                url: '/user_info/update/',
                type: 'POST',
                data: {'password':update_password,'email':update_email,'user':user,'username':username,'update_roles':update_roles},
                dataType: 'json',
                success:function (data) {
                    window.location.href='/user_info'
                    },
                error:function (data) {
                    alert('修改失败')

                }

            })

        })

    }



    function bindUpdateEmail() {

        $('#update_email_put').click(function () {

            var update_email = $("#update_email").val();
            var username = $('#email_username').text();
            $.ajax({
                url: '/update_email/',
                type: 'POST',
                data: {'email':update_email,'username':username},
                dataType: 'json',
                success:function (data) {
                    window.location.href='/index'
                    },
                error:function (data) {
                    alert('输入非法字符')

                }

            })

        })

    }

 function bindAddCron() {
        $('#add_cron').click(function () {
            var add_cron_www_name = $('#add_cron_www_name').val();
            var add_run_time = $('#add_run_time').val();
            var create_username = $('#username').val();
            if (add_run_time.length == 0 || add_cron_www_name.length == 0) {
                alert(create_username)

                }
                else {
                $.ajax({
                    url: "/git_timing/add/",
                    type: "POST",
                    data: {'add_cron_www_name': add_cron_www_name, 'add_run_time': add_run_time },
                    dataType: "json",
                    success:function (data) {
                        location.reload()
                    },
                error:function () {
                    alert('更新失败')
                }

                })}}
        )


    }


    function bindRemoveCron() {
        $('#remove_crom_list').click(function () {
            var del_cron_list=new Array();
            $("input[type='checkbox']:checked").each(function () {
                del_cron_list.push($(this).val())


            })
            if(del_cron_list.length == 0){
                alert('提交不能为空')
            }else {
                $.ajax({
                    url: '/git_timing/delete/',
                    type: "POST",
                    data: {'del_cron_list':del_cron_list},
                    dataType: "json",
                    success: function (data) {
                        location.reload()
                    },
                    error: function () {
                        alert('删除失败')
                    }
                })

            }

        })
    }


 function bindAddRandomPassword() {
        $('#create_random_pass').click(function () {
                $.ajax({
                    url: "/create_password",
                    type: "GET",
                    dataType: "text",
                    success: function (data) {
                        $('.random_password').attr('value',data)
                    },
                    error: function (data) {
                        alert('失败')
                    }

                })}


        )

    }

