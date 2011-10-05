/*global jQuery, flowplayer, window */
(function($) {
function initialVolume() {
    var volume = window.collective_flowplayer.initialVolumePercentage;
    if (volume !== null) {
        this.setVolume(volume);
    }
}
function loop() {
    return !window.collective_flowplayer.loop;
}
$(function() {

    $('.autoFlowPlayer').each(function() {

        $(this).jPlayer({
            ready: function() {
                $(this).jPlayer( "setMedia", {
                    mp3: "http://localhost:8080/jplayer/bla"
                }).jPlayer("play");
            },
            swfPath: "/++resource++collective.jplayer/",
            wmode:"window"

    });
    });

    // $(".autoFlowPlayer").jPlayer({
    //         ready: function (event) {
    //             $(this).jPlayer("setMedia", {
    //                 m4a:"http://www.jplayer.org/audio/m4a/TSP-01-Cro_magnon_man.m4a",
    //                 oga:"http://www.jplayer.org/audio/ogg/TSP-01-Cro_magnon_man.ogg"
    //             });
    //         },
    //         swfPath: "../js",
    //         supplied: "m4a, oga",
    //         wmode: "window"
    //     });




});
}(jQuery));
