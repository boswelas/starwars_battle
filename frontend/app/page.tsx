




export default function Home() {
  return (
    <div>
      <div className="flex flex-col items-center pt-10">
        <h1>Star Wars Battle</h1>
      </div>
      <div className="flex items-center justify-center mt-20">
        <form className="flex">
          <input type="text" placeholder="Search Character" className="mr-2"></input>
        </form>
        <form className="flex">
          <input type="text" placeholder="Search Character" className="mr-2"></input>
        </form>
      </div>
    </div>
  );

}
