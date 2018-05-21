var map_time_label = function(is_track, label, decimal) {
  var unit = 'm';
  var ret = label.toString();
  if (is_track) {
    unit = 's';
    var s = 14;
    var l = 5;
    if (label < 60) {
      s = 17;
    }
    else {
      if (decimal > 0) {
	l = l + 1 + decimal;
      }
    }
    ret = new Date(label * 1000).toISOString().substr(s, l);
  }
  ret = ret.concat(unit);
  return ret;
}

var plot_data = function(ctx, is_track, plot_x, plot_y) {
  chart_type = 'bar';
  if (plot_x.length == 0) {
    return;
  } else if (plot_x.length > 1) {
    chart_type = 'line';
  }
  var myChart = new Chart(ctx, {
    type: chart_type,
    data: {
      labels: plot_x,
      datasets: [{
        data: plot_y,
	backgroundColor: [
	  'rgba(54, 162, 235, 0.2)',
	],
        borderWidth: 1,
      }]
    },
    options: {
      legend: {
        display: false,
      },
      tooltips: {
	enabled: true,
	mode: 'single',
	callbacks: {
	  label: function(tooltipItems, data){
	    var ret = map_time_label(is_track, tooltipItems.yLabel, 2);
	    return ret;
	  }
	}
      },
      scales: {
	yAxes: [
	  {
	    ticks: {
	      callback: function(label){
		var ret = map_time_label(is_track, label, 0);
		return ret;
	      }
	    }
	  }
	]
      },
    }
  });
}