
// Handles json codon data from server
$(document).ready(function () {
    $('#form-data').submit(function (event) {
        event.preventDefault();

        $.ajax({
            type: "POST",
            url: "/counting_codons",
            data: {},
            success: function (data) {
                console.log(data);
                // Your code to process the data
            }
        });
    });
});
