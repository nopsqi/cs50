const NewPost = () => {
    return (
        <form>
            <textarea></textarea>
            <button className="btn btn-primary">Post</button>
        </form>
    )
}

ReactDOM.render(<NewPost />, document.getElementById('new-post'))
