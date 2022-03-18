host = "http://23.21.174.232/"


async function postData(url = '', data = {}) {
    // Default options are marked with *
    console.log(data)
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'no-cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    //   credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
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

    await postData(host + endpoint , {'mssv' : parseInt(mssv)})
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

