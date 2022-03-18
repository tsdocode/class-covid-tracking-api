host = "http://23.21.174.232/"

function setPositiveCase(pos_case){
    $('#f0CasesCount').html(pos_case);
}

const positive_case = async () => {
    const response = await fetch(host + "positive")
        .then(response => response.json())
        .then(data => setPositiveCase(data.data[0]['totalCase']))
}





positive_case();

