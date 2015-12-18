$i(document).ready(function() {

  $i('.tab-content>div:not(":first-of-type")').hide();
  $i('<div class="line"></div>').appendTo('.tab-menu li');
  $i('.tab-menu li:first-of-type').find(':first').width('100%')

  $i('.tab-menu li').each(function(i) {
    $i(this).attr('data-tab', 'tab'+i);
  });

  $i('.tab-content>div').each(function(i) {
    $i(this).attr('data-tab', 'tab'+i);
  });

  $i('.tab-menu li').on('click', function() {

    var dataTab = $i(this).data('tab');
    var getWrapper = $i(this).closest('.tab-wrapper');
    var line = $i(this).find('.line');

    getWrapper.find('.tab-menu li').removeClass('active');
    $i(this).addClass('active');

    getWrapper.find('.line').width(0);
    line.animate({'width':'100%'}, 'fast');
    getWrapper.find('.tab-content>div').hide();
    getWrapper.find('.tab-content>div[data-tab='+dataTab+']').show();
  });

});
