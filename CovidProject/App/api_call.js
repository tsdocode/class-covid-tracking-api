host = "http://23.21.174.232/"


async function postData(url = '', data = {}) {
    var url = "http://23.21.174.232/positive/add";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);

    // xhr.setRequestHeader("accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    // xhr.setRequestHeader("Access-Control-Allow-Origin", "*");

    // xhr.setRequestHeader("mode", "no-cors");

    

    xhr.onreadystatechange = function () {
       if (xhr.readyState === 4) {
          console.log(xhr.status);
          console.log(xhr.responseText);
       }};
    
    var data = `{
      "mssv": 19133001
    }`;
    
    xhr.send(data);
        
}

function set_content(id ,pos_case){
    $("#" + id).html(pos_case);
}

function make_option(id , value){
    $("#" + id).append(`<option value="${value}">${value}</option>`);
}

const positive_case = async () => {
    const response = await fetch(host + "positive")
        .then(response => response.json())
        .then(data => set_content("f0CasesCount" , data.data[0]['totalCase']))
}


const number_of_student = async () => {
    const response = await fetch(host + "student/amount")
        .then(response => response.json())
        .then(data => set_content("memberCount" , data.data[0]['numberOfStudent']))
}

const get_all_mssv = async () => {
    const response = await fetch(host + "student/all")
        .then(response => response.json())
        .then(data => {
            data.data[0].students.forEach(element => {
                make_option("selectMSSV" , element);
            });
        })

}


async function update_status() {
    mssv = $("#selectMSSV").val();
    status = $("#selectStatus").val();

    console.log(status)

    if (status == 1) {
        endpoint = 'positive/add/'
    } else {
        endpoint = 'positive/negative'
    }

    await postData(host + endpoint , {"mssv" : parseInt(mssv)})
        .then(data => {
            console.log(data)
            reload()
        })
}



function reload() {

    positive_case();
    number_of_student();
    get_all_mssv();
}


get_all_mssv();
number_of_student();
positive_case();

