// Logic to style country field

let countrySelected = document.getElementById('id_default_country').value;
if(!countrySelected) {
    document.getElementById('id_default_country').style.color = '#aab7c4';
}

document.getElementById('id_default_country').addEventListener('change', function() {
    countrySelected = this.value;
    if (!countrySelected) {
        this.style.color = '#aab7c4';
    } else {
        this.style.color = '#000';
    }
});