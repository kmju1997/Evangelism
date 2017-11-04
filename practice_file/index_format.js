
module.exports = function (context, req) {
 
    if (            ) {    // If the two persons in the pictures is identical
        var confidence = (             )*100; // confidence variable
        context.res = {
            body: "The two people in the pictures is identical. Resemblance is" + parseInt(          ) +"%." // respond
        };
    }
    else {   // If the two persons in the pictures is not identical
        var confidence = (             )*100; //  confidence variable
        context.res = {
            body: "The two persons in the pictures is not identical. Resemblance is " + parseInt(          ) +"%." // respond     
        };
    }
    context.done();
};

