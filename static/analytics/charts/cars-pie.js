// Espera a que el DOM esté completamente cargado antes de ejecutar el script
document.addEventListener('DOMContentLoaded', function () {
  // Establecer los valores por defecto de la fuente y el color para imitar el estilo de Bootstrap
  Chart.defaults.global.defaultFontFamily =
    'Nunito, -apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
  Chart.defaults.global.defaultFontColor = '#858796';

  // Encuentra el elemento canvas
  var ctx = document.getElementById('carsPieChart');

  // IMPORTANTE: Solo continuar si el elemento canvas existe en esta página
  if (ctx) {
    // Leer los datos desde los atributos data-* del canvas
    const withContract = parseInt(ctx.dataset.withContract) || 0;
    const withoutContract = parseInt(ctx.dataset.withoutContract) || 0;

    // Crear el gráfico
    var myPieChart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['Con Contrato', 'Sin Contrato'],
        datasets: [
          {
            data: [withContract, withoutContract],
            backgroundColor: ['#4e73df', '#1cc88a'],
            hoverBackgroundColor: ['#2e59d9', '#17a673'],
            hoverBorderColor: 'rgba(234, 236, 244, 1)'
          }
        ]
      },
      options: {
        maintainAspectRatio: false,
        tooltips: {
          backgroundColor: 'rgb(255,255,255)',
          bodyFontColor: '#858796',
          borderColor: '#dddfeb',
          borderWidth: 1,
          xPadding: 15,
          yPadding: 15,
          displayColors: false,
          caretPadding: 10
        },
        legend: {
          display: false
        },
        cutoutPercentage: 80
      }
    });
  }
});
