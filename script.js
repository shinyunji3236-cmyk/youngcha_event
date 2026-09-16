/**
 * 영등포 전통시장 with 영차 (0-cha 💜)
 * 공식 인터랙션 스크립트 (script.js)
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. 헤더 스크롤 효과
  const header = document.querySelector('.header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header?.classList.add('scrolled');
    } else {
      header?.classList.remove('scrolled');
    }
  });

  // 2. 모바일 햄버거 메뉴 토글
  const menuToggle = document.querySelector('.menu-toggle');
  const navMobile = document.querySelector('.nav-mobile');
  
  if (menuToggle && navMobile) {
    menuToggle.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
      navMobile.classList.toggle('open');
    });

    // 모바일 메뉴 링크 클릭 시 메뉴 닫기
    navMobile.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menuToggle.classList.remove('active');
        navMobile.classList.remove('open');
      });
    });
  }

  // 3. D-Day 카운트다운 (2026-09-18 13:00:00 KST 기준)
  const targetDate = new Date('2026-09-18T13:00:00+09:00').getTime();
  const ddayDays = document.getElementById('dday-days');
  const ddayHours = document.getElementById('dday-hours');
  const ddayMinutes = document.getElementById('dday-minutes');
  const ddaySeconds = document.getElementById('dday-seconds');

  function updateCountdown() {
    const now = new Date().getTime();
    const distance = targetDate - now;

    if (distance < 0) {
      const ddayBox = document.querySelector('.dday-box');
      if (ddayBox) {
        ddayBox.innerHTML = '<span class="dday-title">🎉 영차 팝업 & 야시장 진행 중! 어서 오세요!</span>';
      }
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    if (ddayDays) ddayDays.textContent = String(days).padStart(2, '0');
    if (ddayHours) ddayHours.textContent = String(hours).padStart(2, '0');
    if (ddayMinutes) ddayMinutes.textContent = String(minutes).padStart(2, '0');
    if (ddaySeconds) ddaySeconds.textContent = String(seconds).padStart(2, '0');
  }

  if (ddayDays) {
    updateCountdown();
    setInterval(updateCountdown, 1000);
  }

  // 4. 스크롤 트리거 페이드업 애니메이션 (Intersection Observer)
  const observerOptions = {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.fade-in-section, .event-card, .story-card, .chuseok-card, .map-wrapper, .store-story-section').forEach(el => {
    el.classList.add('fade-in-section');
    observer.observe(el);
  });

  // 5. 카드뉴스 모달 뷰어 (Lightbox)
  const modal = document.getElementById('cardModal');
  const modalImg = document.getElementById('modalImage');
  const closeBtn = document.querySelector('.modal-close-btn');
  const prevBtn = document.querySelector('.modal-prev');
  const nextBtn = document.querySelector('.modal-next');

  let currentGalleryImages = [];
  let currentImageIndex = 0;

  function openModal(imgSrcList, startIndex) {
    if (!modal || !modalImg) return;
    currentGalleryImages = imgSrcList;
    currentImageIndex = startIndex;
    modalImg.src = currentGalleryImages[currentImageIndex];
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  function showNextImage() {
    if (currentGalleryImages.length === 0) return;
    currentImageIndex = (currentImageIndex + 1) % currentGalleryImages.length;
    modalImg.src = currentGalleryImages[currentImageIndex];
  }

  function showPrevImage() {
    if (currentGalleryImages.length === 0) return;
    currentImageIndex = (currentImageIndex - 1 + currentGalleryImages.length) % currentGalleryImages.length;
    modalImg.src = currentGalleryImages[currentImageIndex];
  }

  // 갤러리 아이템 클릭 시 모달 연동
  document.querySelectorAll('[data-gallery]').forEach(galleryContainer => {
    const galleryItems = galleryContainer.querySelectorAll('.gallery-item, .cardnews-img-wrap');
    const images = Array.from(galleryItems).map(item => {
      const img = item.querySelector('img');
      return img ? img.getAttribute('src') : '';
    }).filter(Boolean);

    galleryItems.forEach((item, index) => {
      item.addEventListener('click', () => {
        openModal(images, index);
      });
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });
  }
  if (nextBtn) nextBtn.addEventListener('click', (e) => { e.stopPropagation(); showNextImage(); });
  if (prevBtn) prevBtn.addEventListener('click', (e) => { e.stopPropagation(); showPrevImage(); });

  // 키보드 내비게이션 지원
  window.addEventListener('keydown', (e) => {
    if (!modal || !modal.classList.contains('active')) return;
    if (e.key === 'Escape') closeModal();
    if (e.key === 'ArrowRight') showNextImage();
    if (e.key === 'ArrowLeft') showPrevImage();
  });

  // 터치 스와이프 지원 (모바일 제스처)
  let touchStartX = 0;
  let touchEndX = 0;

  if (modal) {
    modal.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    modal.addEventListener('touchend', (e) => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, { passive: true });
  }

  function handleSwipe() {
    const swipeThreshold = 50;
    if (touchEndX < touchStartX - swipeThreshold) {
      showNextImage(); // 좌측 스와이프 -> 다음 이미지
    }
    if (touchEndX > touchStartX + swipeThreshold) {
      showPrevImage(); // 우측 스와이프 -> 이전 이미지
    }
  }

  // 6. 주소 복사 기능
  const copyBtn = document.getElementById('copyAddressBtn');
  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      const address = "서울특별시 영등포구 영등포동 618-296 영등포전통시장";
      navigator.clipboard.writeText(address).then(() => {
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '✅ 복사 완료!';
        setTimeout(() => {
          copyBtn.innerHTML = originalText;
        }, 2000);
      }).catch(err => {
        console.error('주소 복사 실패:', err);
      });
    });
  }
});
