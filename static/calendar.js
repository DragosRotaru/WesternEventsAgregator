$(function () {
	var date = new Date();
	var d = date.getDate();
	var m = date.getMonth();
	var y = date.getFullYear();

	$('#calendar').fullCalendar({
		header: {
			left: 'prev,next today',
			center: 'title',
			right: 'month,agendaWeek,agendaDay'
		},
		editable: false
	});
	$('#calendar').fullCalendar({
    		dayClick: function() {
        		alert('a day has been clicked!');
		}
	});
});
