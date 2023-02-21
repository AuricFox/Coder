// Toggles display of sub navigation elements

var navDisplay = {
    display: 'flex',
    flexDirection: 'row'
};

$('#bio-pages').click(() => {
    $('.sub-nav').not($('#bio-nav')).hide();

    if($('#bio-nav').is(':visible')) {$('#bio-nav').hide();}
    else {$('#bio-nav').css(navDisplay).show();}
});

// ----------------------------------------------------------
$('#chem-pages').click(() => {
    $('.sub-nav').not($('#chem-nav')).hide();

    if($('#chem-nav').is(':visible')) {$('#chem-nav').hide();}
    else {$('#chem-nav').css(navDisplay).show();}
});

// ----------------------------------------------------------
$('#csci-pages').click(() => {
    $('.sub-nav').not($('#csci-nav')).hide();

    if($('#csci-nav').is(':visible')) {$('#csci-nav').hide();}
    else {$('#csci-nav').css(navDisplay).show();}
});

// ----------------------------------------------------------
$('#eng-pages').click(() => {
    $('.sub-nav').not($('#eng-nav')).hide();

    if($('#eng-nav').is(':visible')) {$('#eng-nav').hide();}
    else {$('#eng-nav').css(navDisplay).show();}
});

// ----------------------------------------------------------
$('#math-pages').click(() => {
    $('.sub-nav').not($('#math-nav')).hide();

    if($('#math-nav').is(':visible')) {$('#math-nav').hide();}
    else {$('#math-nav').css(navDisplay).show();}
});

// ----------------------------------------------------------
$('#tools-pages').click(() => {
    $('.sub-nav').not($('#tools-nav')).hide();

    if($('#tools-nav').is(':visible')) {$('#tools-nav').hide();}
    else {$('#tools-nav').css(navDisplay).show();}
});