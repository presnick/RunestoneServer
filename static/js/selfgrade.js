function selfGrade(assignment_id, student_id) {
    var enforceDeadline = false     // don't enforce assignment deadlines for self-grading in Coursera MOOC; should be taken from config
    jQuery.ajax({
        url: eBookConfig.autogradingURL,
        type: "POST",
        dataType: "JSON",
        data: {
            assignment_id: assignment_id,
            question: null,
            sid: student_id,
            enforceDeadline: enforceDeadline
        },
        success: function (retdata) {
            window.location.reload(true);
        }
    });
}