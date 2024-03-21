async function bot_start() {
    var token = $('#discord_token').val();
    var key = $('#api_key').val();
    var engine = $('#engine_chatbot').val();
    var chanel = $('#chanel_id').val();
    const status = await eel.Bot_Status()();
    if (status == 'Online') {
        Swal.fire({
            title: "Error!",
            text: "Bot still Online!",
            icon: "error",
            confirmButtonText: "OK"
        });
        logger("Can't start bot still Online")
    } else {
        if (token !== "" && key !== "" && engine !== "" && chanel !== "") {
            eel.Bot_Start(engine, token, key, chanel);
            Swal.fire({
                title: "Success!",
                text: "Bot gonna running!",
                icon: "success",
                confirmButtonText: "OK"
            });
            update_status();
            logger("Start bot successful , Update status Online")
        } else {
            Swal.fire({
                title: "Error!",
                text: "Token or key is empty!",
                icon: "error",
                confirmButtonText: "OK"
            });
            logger("Error! Token or key is empty!")
        }
    }


}
async function bot_stop() {
    const status = await eel.Bot_Status()();
    if (status == 'Offline') {
        Swal.fire({
            title: "Error!",
            text: "Bot still Offline!",
            icon: "error",
            confirmButtonText: "OK"
        });
        logger("Can't stop bot still Offline")
    } else {
        eel.Bot_Stop()
        Swal.fire({
            title: "Success!",
            text: "Stop bot successfully",
            icon: "success",
            confirmButtonText: "OK"
        });
        update_status();
        logger("Stop bot successful , Update status Offline")
    }
}

async function bot_log() {
    var data = $('#discord_token').val();
    eel.Bot_Log()
}

async function loadSettings() {
    const data = await eel.properties_read()();
    if (data) {
        $('#discord_token').val(data["token"]);
        $('#api_key').val(data["key"]);
        $('#engine_chatbot').val(data["engine"]);
        $('#chanel_id').val(data["chanel"]);
    }
}

async function update_status() {
    const text = $('#bot-status');
    const status = await eel.Bot_Status()();
    if (status == 'Online') {
        $(text).text('Online');
        $(text).removeClass('bg-danger').addClass('bg-success');
    } else if (status == 'Offline') {
        $(text).text('Offline');
        $(text).removeClass('bg-success').addClass('bg-danger');
    }
}

async function logger(message) {
    eel.Message_Callbace(message)();
}


$("#toggle_token").click(function() {
    var inputField = $("#discord_token");
    var currentType = inputField.attr("type");
    var newType = currentType === "password" ? "text" : "password";
    inputField.attr("type", newType);

    $(this).find("i").toggleClass("fa-eye fa-eye-slash");
});

$("#toggle_key").click(function() {
    var inputField = $("#api_key");
    var currentType = inputField.attr("type");
    var newType = currentType === "password" ? "text" : "password";
    inputField.attr("type", newType);

    $(this).find("i").toggleClass("fa-eye fa-eye-slash");
});

loadSettings();
update_status();