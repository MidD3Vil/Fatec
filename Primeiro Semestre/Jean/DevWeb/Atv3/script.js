const menubtn = document.querySelector('.menu')
menu = document.querySelector('header ul')
up = document.querySelector('.up')

menubtn.onclick = function() {
  if (!menu.classList.contains('open')) {
    menu.classList.add('open')
    menubtn.style.transform = 'rotate(180deg)'
    menubtn.classList.remove('uil-bars')
    menubtn.classList.add('uil-times')
  } else {
    menu.classList.remove('open')
    menubtn.style.transform = 'rotate(0deg)'
    menubtn.classList.add('uil-bars')
    menubtn.classList.remove('uil-times')
  }
}

window.addEventListener('scroll', () => {
  if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
    up.style.display = "block"
  } else {
    up.style.display = "none"
  }
  if (menu.classList.contains('open')) {
    menu.classList.remove('open')
    menubtn.style.transform = 'rotate(0deg)'
    menubtn.classList.add('uil-bars')
    menubtn.classList.remove('uil-times')
  }
})

up.addEventListener('click', () => {
  document.body.scrollTop = 0
  document.documentElement.scrollTop = 0
})

const nav1 = document.getElementById('nav1')
nav2 = document.getElementById('nav2')
nav3 = document.getElementById('nav3')
nav4 = document.getElementById('nav4')



nav1.onclick = function() {
  menu.classList.remove('open')
  menubtn.style.transform = 'rotate(0deg)'
  menubtn.classList.add('uil-bars')
  menubtn.classList.remove('uil-times')
}
nav2.onclick = function() {
  menu.classList.remove('open')
  menubtn.style.transform = 'rotate(0deg)'
  menubtn.classList.add('uil-bars')
  menubtn.classList.remove('uil-times')
}
nav3.onclick = function() {
  menu.classList.remove('open')
  menubtn.style.transform = 'rotate(0deg)'
  menubtn.classList.add('uil-bars')
  menubtn.classList.remove('uil-times')
}
nav4.onclick = function() {
  menu.classList.remove('open')
  menubtn.style.transform = 'rotate(0deg)'
  menubtn.classList.add('uil-bars')
  menubtn.classList.remove('uil-times')
}


const htmlbar = document.getElementById('bar1')
cssbar = document.getElementById('bar2')
jsbar = document.getElementById('bar3')

window.addEventListener('scroll', () => {
  if (document.body.scrollTop > 1200 || document.documentElement.scrollTop > 1200) {
    htmlbar.classList.add('activehtml')
    cssbar.classList.add('activecss')
    jsbar.classList.add('activejs')
  }
})

const sw = document.querySelector('.switch')
swcircle = document.querySelector('.switchcircle')

sw.addEventListener('click', () => {
  if (!swcircle.classList.contains('on')) {
    swcircle.classList.add('on')
    swcircle.innerHTML = `<ion-icon name="sunny-outline"></ion-icon>`
    document.body.classList.add('dark')
    menu.classList.remove('open')
    menubtn.style.transform = 'rotate(0deg)'
    menubtn.classList.add('uil-bars')
    menubtn.classList.remove('uil-times')
    sw.style.backgroundColor = '#1F2021'
  } else {
    swcircle.classList.remove('on')
    swcircle.innerHTML = `<ion-icon name="moon-outline"></ion-icon>`
    document.body.classList.remove('dark')
    menu.classList.remove('open')
    menubtn.style.transform = 'rotate(0deg)'
    menubtn.classList.add('uil-bars')
    menubtn.classList.remove('uil-times')
    sw.style.backgroundColor = '#fff'
  }
})