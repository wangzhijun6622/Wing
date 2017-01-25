var listClick = function(obj){
		// api.toast({
  //           msg: obj.id,
  //           duration: 2000,
  //           location: 'middle'
  //       });
        switch(obj.id){

            case 'everyDayList': 

                 $api.addCls($api.byId('everyDayList'),'day_active'); 
                 // $api.byId('everyMonList').className=''
                 // $api.byId('everyYearList').className=''
                 break;

            case 'everyMonList': 
                 $api.addCls($api.byId('everyMonList'),'mon_active'); 
                 break;

            case 'everyYearList': 
                 $api.addCls($api.byId('everyYearList'),'year_active'); 
                 break;
            case 'con' :
                $api.removeCls($api.byId('everyDayList'),'day_active');
                $api.removeCls($api.byId('everyMonList'),'mon_active');
                $api.removeCls($api.byId('everyYearList'),'year_active');
                break;
        }
        var objId = obj.id;
        // $api.byId(objId).
        // $api.byId(objId).
        }
//提示信息
var showToast = function(obj){
        api.toast({
            msg: '提示信息!',
            duration: 2000,
            location: 'middle'
        });
    };
var daylist = function(nameH){
    api.ajax({
            url: 'http://10.131.11.139:10000/reminder/daily/index/',
            method: 'get',
            data: {}
        },function(ret, err){
            if (ret) {
                if(ret.code==0){
                    var todayList_ul = $api.byId('tadyList_ul');
                    var mainright_li = document.createElement('li')
                    var today =  ret.data.today ;
                    if(nameH=="wing_add_daylist"){
                        var mainLeft_ul = $api.byId('mainLeft_ul');
                        var mainLeft_li = document.createElement('li')
                        var history =  ret.data.history ;
                        for(var i=0;i<history.length;i++){
                            var li_inputLeft = document.createElement('input')
                            li_inputLeft.setAttribute('data-id',history[i].id);
                            li_inputLeft.value = history[i].content;
                            li_inputLeft.setAttribute('disabled',"disabled");
                            mainLeft_li.appendChild(li_inputLeft);
                            mainLeft_ul.appendChild(mainLeft_li);
                        }
                        for(var i=0;i<today.length;i++){
                            var li_input = document.createElement('input')
                            li_input.setAttribute('data-id',today[i].id);
                            li_input.value = today[i].content;
                            li_input.setAttribute('onblur',"saveDayThis(this)");
                            mainright_li.appendChild(li_input)
                            todayList_ul.appendChild(mainright_li);
                        }
                    }else{
                        for(var i=0;i<today.length;i++){
                          var li_input = document.createElement('input')
                          li_input.setAttribute('data-id',today[i].id);
                          li_input.value = today[i].content;
                          li_input.setAttribute('disabled',"disabled");
                          li_input.setAttribute('display',"block");
                          mainright_li.appendChild(li_input)
                          todayList_ul.appendChild(mainright_li);
                        }
                    }
                  }
            } else {
                alert( JSON.stringify( err ) );
            }
        });
}