class OceanHunter
  constructor: ->

  # after you change the content in the fixed-to-bottom-wrapper,
  # you have to call this again
  reAdjustFixedBottom: ->
    $('body').css 'padding-bottom', ->
      $('.fixed-to-bottom-wrapper').height()

  _showFixedBottom: ->
    $('.fixed-to-bottom-wrapper')
      .css 'opacity', 1


$ ->
  window.oh = new OceanHunter
  oh.reAdjustFixedBottom()
  oh._showFixedBottom()