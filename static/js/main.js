document.querySelectorAll('.like-btn').forEach(btn => {
    const likeCount = btn.parentElement.querySelector('.like-count');
    const count = parseInt(likeCount.textContent);
    
    // Set initial state if already liked
    if (count > 0) {
        btn.classList.add('liked');
    }
    
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        const postId = this.dataset.postId;
        
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
        
        fetch(`/posts/post/${postId}/like/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
        .then(response => response.json())
        .then(data => {
            likeCount.textContent = data.like_count;
            
            // Add animation
            btn.classList.add('animate');
            setTimeout(() => btn.classList.remove('animate'), 600);
            
            // Toggle liked state
            if (data.like_count > 0) {
                btn.classList.add('liked');
            } else {
                btn.classList.remove('liked');
            }
        });
    });
});