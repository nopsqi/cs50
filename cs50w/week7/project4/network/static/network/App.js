const App = () => {
    const [state, setState] = React.useState({
        api: new URL(document.getElementById('App').dataset.api, document.location.origin),
        loading: true

    })

    React.useEffect(() => {
        setState({
            ...state,
            loading: false
        })

        fetch(state.api)
        .then(response => {
            if (response.status == 200) {
                response.json()
                .then(result => {
                    console.log(result)

                    setState({
                        ...state,
                        ...result,
                        loading: true,
                    })
                })
            }
        })
    }, [])

    const addPost = () => {
        setState({
            ...state,
            posts: [...state.posts, state.posts[state.posts.length-1] + 1]
        })
    }

    if (state.loading) {
        return (<div></div>)
    }

    return (
        <div>
            <NewPost onClick={addPost} />
            <Posts posts={state.posts}/>
            <Paginator />
        </div>
    )
}

const NewPost = (props) => {
    return (
        <div>
            <h1>NEW POST HOLDER</h1>
        </div>
    )
}

const Posts = (props) => {
    return (
        <div>
            <h1>POSTS HOLDER</h1>
            {props.posts.map((item, index) => (
                <Post />
            ))}
        </div>
    )
}

const Post = (props) => {
    return (
        <div>
            <h2>POST HOLDER</h2>
        </div>
    )
}

const Paginator = () => {
    return (
        <div>
            <h1>PAGINATOR HOLDER</h1>
        </div>
    )
}

ReactDOM.render(<App />, document.getElementById('App'))
