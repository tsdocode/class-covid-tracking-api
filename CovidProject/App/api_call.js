host = "http://23.21.174.232/"

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
            data.data['students'].forEach(element => {
                make_option("selectMSSV" , element.mssv);
            });
        })

}





get_all_mssv();
number_of_student();
positive_case();

