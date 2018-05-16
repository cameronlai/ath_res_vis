var plot_data = function(ctx, plot_x, plot_y) {
  console.log(plot_x);
  console.log(plot_y);

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
        borderWidth: 1
      }]
    },
    options: {
      legend: {
        display: false
      },
    }
  });
}