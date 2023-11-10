const App = () => {
    const [state, setState] = React.useState({
        api: new URL(document.getElementById('App').dataset.api, document.location.origin)
    })

    React.useEffect(() => {
        fetch(`${state.api.pathname}/${state.api.search}`)
    }, [])

    api.searchParams.append('page', 1)

    return (
        <div>
            <h1>{state.api.origin}</h1>
            <NewPost />
            <Posts />
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

const Posts = () => {
    return (
        <div>
            <h1>POSTS HOLDER</h1>
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
