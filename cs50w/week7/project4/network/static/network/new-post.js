const NewPost = () => {
    const [state, setState] = React.useState({value: ""})

    const onSubmit = (e) => {
        e.preventDefault()
    }

    return (
        <form className="mt-3 text-right" onSubmit={onSubmit}>
            <textarea type="text" className="form-control" value={state.value} onChange={(e) => {setState({value: e.target.value})}}></textarea>
            <button type="submit" className="mt-2 btn btn-primary">Post</button>
        </form>
    )
}

ReactDOM.render(<NewPost />, document.getElementById('new-post'))
