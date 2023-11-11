const App = () => {
    const [state, setState] = React.useState({
        api: new URL(document.getElementById('App').dataset.api, document.location.origin),
        loading: true,
    })

    React.useEffect(() => {
        setState({
            ...state,
            loading: true
        })

        fetch(state.api)
        .then(response => {
            console.log("fetching", state.api.href)
            if (response.status == 200) {
                response.json()
                .then(result => {
                    setState({
                        ...state,
                        loading: false,
                        ...result,
                    })
                })
            } else {
                console.log(result)
            }
        })
    }, [])

    console.log(state)

    const addPost = (e) => {
        setState({
            ...state,
            posts: [...state.posts, {id: 17}]
        })
    }

    const deletePost = (e) => {
        setState({
            posts: state.posts.filter((item, index) => item.id !== parseInt(e.target.parentElement.childNodes[1].innerHTML))
        })
    }

    if (state.loading) {
        return (<div></div>)
    }

    const changeURL = () => {
        let page = parseInt(state.api.searchParams.get('page'))
        // const api = new URL(state.api.href)
        const api = state.api
        api.searchParams.set('page', page + 1)
        setState({
            ...state,
            api: api
        })

    }

    return (
        <div>
            <h1>APP HOLDER</h1>
            <h2>{state.api.href}</h2>
            <button onClick={changeURL}>Change URL</button>
            <NewPost onClick={addPost} />
            <Posts posts={state.posts} onClick={deletePost}/>
            <Paginator />
        </div>
    )
}

const NewPost = (props) => {
    return (
        <div>
            <h2>NEW POST HOLDER</h2>
            <button onClick={props.onClick}>Add Post</button>
        </div>
    )
}

const Posts = (props) => {
    return (
        <div>
            <h2>POSTS HOLDER</h2>
            {props.posts.map((post, index) => (
                <Post key={index} {...post} onClick={props.onClick}/>
            ))}
        </div>
    )
}

const Post = (props) => {
    return (
        <div>
            <h3>POST HOLDER</h3>
            <div>{props.id}</div>
            <button onClick={props.onClick}>Delete</button>
        </div>
    )
}

const Paginator = () => {
    return (
        <div>
            <h2>PAGINATOR HOLDER</h2>
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))
