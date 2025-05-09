/**
 * Script para manejar las interacciones con los modales de análisis y sesgo
 */

document.addEventListener('DOMContentLoaded', function() {
  // Referencias a los botones y modales
  const btnAnalisis = document.querySelector('.action-btn svg[xlink\\:href="#cpu-fill"]')?.closest('.action-btn');
  const btnSesgo = document.querySelector('.action-btn svg[xlink\\:href="#toggles2"]')?.closest('.action-btn');
  const analisisModal = new bootstrap.Modal(document.getElementById('analisisModal'));
  const sesgoModal = new bootstrap.Modal(document.getElementById('sesgoModal'));
  
  // Referencias a elementos dentro de los modales
  const verSesgoBtn = document.getElementById('ver-sesgo-btn');
  const verAnalisisBtn = document.getElementById('ver-analisis-btn');
  
  let currentNoticiaId = null;
  
  // Configurar eventos de cambio entre modales
  if (verSesgoBtn) {
    verSesgoBtn.addEventListener('click', function() {
      analisisModal.hide();
      loadSesgoData(currentNoticiaId);
      setTimeout(() => sesgoModal.show(), 500);
    });
  }
  
  if (verAnalisisBtn) {
    verAnalisisBtn.addEventListener('click', function() {
      sesgoModal.hide();
      loadAnalisisData(currentNoticiaId);
      setTimeout(() => analisisModal.show(), 500);
    });
  }
  
  // Añadir event listeners a los botones principales
  if (btnAnalisis) {
    btnAnalisis.addEventListener('click', function() {
      currentNoticiaId = this.getAttribute('data-id');
      loadAnalisisData(currentNoticiaId);
      analisisModal.show();
    });
  }
  
  if (btnSesgo) {
    btnSesgo.addEventListener('click', function() {
      currentNoticiaId = this.getAttribute('data-id');
      loadSesgoData(currentNoticiaId);
      sesgoModal.show();
    });
  }
  
  /**
   * Carga los datos de análisis de contenido desde la API
   */
  function loadAnalisisData(noticiaId) {
    // Mostrar el spinner y ocultar el contenido
    document.getElementById('analisis-loading').style.display = 'block';
    document.getElementById('analisis-content').style.display = 'none';
    
    fetch(`/api/noticia/analisis/${noticiaId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Error en la respuesta del servidor');
        }
        return response.json();
      })
      .then(data => {
        // Asignar datos a los elementos del modal
        document.getElementById('analisis-titulo').textContent = data.titulo;
        document.getElementById('analisis-resumen').textContent = data.analisis || 'No hay análisis disponible para esta noticia.';
        document.getElementById('analisis-tipo').textContent = data.tipo || 'No determinado';
        
        // Procesar palabras clave
        const keywordsContainer = document.getElementById('analisis-keywords');
        if (data.keywords) {
          const keywords = data.keywords.split(',').map(k => k.trim()).filter(k => k.length > 0);
          if (keywords.length > 0) {
            keywordsContainer.innerHTML = keywords.map(keyword => 
              `<span class="badge bg-light text-dark analysis-badge">${keyword}</span>`
            ).join('');
          } else {
            keywordsContainer.textContent = 'No hay palabras clave definidas.';
          }
        } else {
          keywordsContainer.textContent = 'No hay palabras clave definidas.';
        }
        
        // Procesar etiquetas
        const tagsContainer = document.getElementById('analisis-tags');
        if (data.tags) {
          const tags = data.tags.split(',').map(t => t.trim()).filter(t => t.length > 0);
          if (tags.length > 0) {
            tagsContainer.innerHTML = tags.map(tag => 
              `<span class="badge bg-dark analysis-badge">${tag}</span>`
            ).join('');
          } else {
            tagsContainer.textContent = 'No hay etiquetas definidas.';
          }
        } else {
          tagsContainer.textContent = 'No hay etiquetas definidas.';
        }
        
        // Ocultar el spinner y mostrar el contenido
        document.getElementById('analisis-loading').style.display = 'none';
        document.getElementById('analisis-content').style.display = 'block';
      })
      .catch(error => {
        console.error('Error al cargar datos de análisis:', error);
        document.getElementById('analisis-loading').style.display = 'none';
        document.getElementById('analisis-content').style.display = 'block';
        document.getElementById('analisis-resumen').textContent = 'Error al cargar el análisis. Por favor, inténtelo de nuevo.';
        toastr.error('Ha ocurrido un error al cargar el análisis.');
      });
  }
  
  /**
   * Carga los datos de análisis de sesgo desde la API
   */
  function loadSesgoData(noticiaId) {
    // Mostrar el spinner y ocultar el contenido
    document.getElementById('sesgo-loading').style.display = 'block';
    document.getElementById('sesgo-content').style.display = 'none';
    
    fetch(`/api/noticia/sesgo/${noticiaId}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Error en la respuesta del servidor');
        }
        return response.json();
      })
      .then(data => {
        // Asignar datos a los elementos del modal
        document.getElementById('sesgo-titulo').textContent = data.titulo;
        
        // Procesar datos de sesgo
        const sesgoData = data.sesgo;
        
        // Tipo principal de sesgo
        const tipoElement = document.getElementById('principal-sesgo-tipo');
        if (sesgoData && sesgoData.tipo_principal) {
          tipoElement.textContent = sesgoData.tipo_principal;
        } else {
          tipoElement.textContent = 'No se ha detectado un sesgo principal';
        }
        
        // Espectro político
        const marker = document.getElementById('marker');
        if (sesgoData && typeof sesgoData.espectro_politico === 'number') {
          // Convertir el valor (-1 a 1) a posición en el espectro (0% a 100%)
          const position = ((sesgoData.espectro_politico + 1) / 2) * 100;
          marker.style.left = `${position}%`;
        } else {
          marker.style.left = '50%'; // Centro por defecto
        }
        
        // Análisis detallado
        const detailElement = document.getElementById('detailedAnalysis');
        if (sesgoData && sesgoData.analisis_detallado) {
          detailElement.innerHTML = `<p>${sesgoData.analisis_detallado}</p>`;
        } else {
          detailElement.innerHTML = '<p>No hay análisis detallado disponible.</p>';
        }
        
        // Configurar gráficos
        setupCharts(sesgoData);
        
        // Ocultar el spinner y mostrar el contenido
        document.getElementById('sesgo-loading').style.display = 'none';
        document.getElementById('sesgo-content').style.display = 'block';
      })
      .catch(error => {
        console.error('Error al cargar datos de sesgo:', error);
        document.getElementById('sesgo-loading').style.display = 'none';
        document.getElementById('sesgo-content').style.display = 'block';
        document.getElementById('principal-sesgo-tipo').textContent = 'Error al cargar el análisis de sesgo.';
        toastr.error('Ha ocurrido un error al cargar el análisis de sesgo.');
      });
  }
  
  /**
   * Configura los gráficos para el análisis de sesgo
   */
  function setupCharts(sesgoData) {
    // Gráfico de emociones
    if (sesgoData && sesgoData.emociones) {
      // Destruir gráfico anterior si existe
      if (window.emotionsChart) {
        window.emotionsChart.destroy();
      }
      
      const emotionsCtx = document.getElementById('emotionsChart').getContext('2d');
      window.emotionsChart = new Chart(emotionsCtx, {
        type: 'pie',
        data: {
          labels: Object.keys(sesgoData.emociones),
          datasets: [{
            data: Object.values(sesgoData.emociones),
            backgroundColor: [
              '#4bc0c0', '#ff6384', '#ffcd56', '#36a2eb', '#9966ff', '#ff9f40'
            ]
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'right'
            }
          }
        }
      });
    }
    
    // Gráfico de temas
    if (sesgoData && sesgoData.temas) {
      // Destruir gráfico anterior si existe
      if (window.topicsChart) {
        window.topicsChart.destroy();
      }
      
      const topicsCtx = document.getElementById('topicsChart').getContext('2d');
      window.topicsChart = new Chart(topicsCtx, {
        type: 'bar',
        data: {
          labels: Object.keys(sesgoData.temas),
          datasets: [{
            label: 'Relevancia',
            data: Object.values(sesgoData.temas),
            backgroundColor: '#8884d8'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
              max: 1
            }
          }
        }
      });
    }
  }
});