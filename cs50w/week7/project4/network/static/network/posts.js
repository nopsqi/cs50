const Posts = () => {
    const url = new URL(document.getElementById('posts').dataset.api, window.location.origin)
    url.searchParams.append('page', 1)

    const [state, setState] = React.useState({
        url: url,
        pages: 0,
        posts: [],
        loading: true,
        update: true,
        newPost: "",
    });

    const allPostsNav = document.getElementById('all-posts-nav')
    const followingNav = document.getElementById('following-nav')

    React.useEffect(() => {
        if (document.location.pathname !== '/') {
            allPostsNav.style.display = 'none';
            followingNav.style.display = 'none';
        } else {
            allPostsNav.style.display = 'block';
            allPostsNav.classList.add('active')
            followingNav.style.display = 'block';
        }

    }, [])

    React.useEffect(() => {
        fetch(state.url.pathname + state.url.search)
        .then(response => response.json())
        .then(result => {
            setState({
                ...state,
                ...result,
                loading: false
            })
        })
    }, [state.url, state.update]);

    const setStateURL = (key, value) => setState(prevState => {
        const url = new URL(prevState.url.pathname + prevState.url.search, prevState.url.origin)
        url.searchParams.set(key, value)
        return {
            ...prevState,
            url: url
        }
    })


    allPostsNav.onclick = (e) => {
        e.preventDefault()
        setStateURL('following', false)
        e.target.classList.add('active')
        followingNav.classList.remove('active')
    }

    followingNav.onclick = (e) => {
        e.preventDefault()
        setStateURL('following', true)
        e.target.classList.add('active')
        allPostsNav.classList.remove('active')
    }

    const goToPage = (e) => {
        e.preventDefault();
        setStateURL('page', e.target.innerHTML)
    }

    const newPostChange = (e) => {
        setState({
            ...state,
            newPost: e.target.value
        })
    }

    const newPostSubmit = (e) => {
        fetch('/api/post', {
            method: 'POST',
            body: JSON.stringify({
                content: e.target[0].value
            })
        })
        .then(response => {
            if (response.status == 200) {
                response.json()
                .then(result => {
                    setState({
                        ...state,
                        newPost: "",
                        update: !state.update,
                    })

                })
            }
        })
        e.preventDefault();
    }

    if (state.loading) {
        return (
            <div>Loading...</div>
        )
    }

    return (
        <div className="mt-3">
            <NewPost onSubmit={newPostSubmit} onChange={newPostChange} value={state.newPost}/>
            {
                state.posts.length > 0
                ? state.posts.map((item, i) => (
                    <Post {...item} />
                ))
                : <p>There are no post yet.</p>
            }
            <Paginator page={state.page} pages={state.pages} onClick={goToPage} />
        </div>
    );
}

const NewPost = (props) => {

    return (
        <form className="mt-3 text-right" onSubmit={props.onSubmit}>
            <textarea type="text" className="form-control" value={props.value} onChange={props.onChange}></textarea>
            <button type="submit" className="mt-2 btn btn-primary">Post</button>
        </form>
    )
}

const Paginator = (props) => {
    const [state, setState] = React.useState(props);

    React.useEffect(() => {
        setState(props);
    }, [props]);

    return (
        <nav className="mt-3" aria-label="Post navigaioon">
            <ul className="pagination justify-content-end">
                {Array.from({length: state.pages}, (_, i) => i + 1).map((item) => (
                    <li key={item} className={`page-item ${item === state.page ? 'active' : ''}`}>
                        <a className="page-link" href="" onClick={state.onClick}>{item}</a>
                    </li>
                ))}
            </ul>
        </nav>
    );
}

const Post = (props) => {
    const [state, setState] = React.useState(props);

    React.useEffect(() => {
        setState({
            ...props,
            like_count: props.likes.length
        })
    }, [props])

    const heart = {
        before: (
            '<svg syle="fill: #1a2a47" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M225.8 468.2l-2.5-2.3L48.1 303.2C17.4 274.7 0 234.7 0 192.8v-3.3c0-70.4 50-130.8 119.2-144C158.6 37.9 198.9 47 231 69.6c9 6.4 17.4 13.8 25 22.3c4.2-4.8 8.7-9.2 13.5-13.3c3.7-3.2 7.5-6.2 11.5-9c0 0 0 0 0 0C313.1 47 353.4 37.9 392.8 45.4C462 58.6 512 119.1 512 189.5v3.3c0 41.9-17.4 81.9-48.1 110.4L288.7 465.9l-2.5 2.3c-8.2 7.6-19 11.9-30.2 11.9s-22-4.2-30.2-11.9zM239.1 145c-.4-.3-.7-.7-1-1.1l-17.8-20c0 0-.1-.1-.1-.1c0 0 0 0 0 0c-23.1-25.9-58-37.7-92-31.2C81.6 101.5 48 142.1 48 189.5v3.3c0 28.5 11.9 55.8 32.8 75.2L256 430.7 431.2 268c20.9-19.4 32.8-46.7 32.8-75.2v-3.3c0-47.3-33.6-88-80.1-96.9c-34-6.5-69 5.4-92 31.2c0 0 0 0-.1 .1s0 0-.1 .1l-17.8 20c-.3 .4-.7 .7-1 1.1c-4.5 4.5-10.6 7-16.9 7s-12.4-2.5-16.9-7z"/></svg>'
        ),
        after: (
            '<svg style="fill: #fd3a3a" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M47.6 300.4L228.3 469.1c7.5 7 17.4 10.9 27.7 10.9s20.2-3.9 27.7-10.9L464.4 300.4c30.4-28.3 47.6-68 47.6-109.5v-5.8c0-69.9-50.5-129.5-119.4-141C347 36.5 300.6 51.4 268 84L256 96 244 84c-32.6-32.6-79-47.5-124.6-39.9C50.5 55.6 0 115.2 0 185.1v5.8c0 41.5 17.2 81.2 47.6 109.5z"/></svg>'
        )
    };

    const switchLike = (e) => {
        e.preventDefault()
        setState({
            ...state,
            like: !state.like,
            like_count: state.like ? state.like_count - 1 : state.like_count + 1
        })
    }
    return (
        <div className="card mt-2">
            <div className="card-body">
                <a href={`${document.location.origin}/${state.username}`} className="text-card">{state.username}</a>
                <div className="text-card">{state.content}</div>
                <div className="d-flex align-items-center">
                    <div className="text-card text-muted">{state.modified}</div>
                    <a href="" className="text-card d-flex ml-5" onClick={switchLike} dangerouslySetInnerHTML={{ __html: state.like ? heart.after : heart.before }} />
                    <div className="text-card ml-2">Like {state.like_count}</div>
                </div>
            </div>
        </div>
    );
}

ReactDOM.render(<Posts />, document.querySelector('#posts'));
