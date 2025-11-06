export default function Home() {
  const randoV = Math.random();
  return (
    <div className="font-sans grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20">
      <main className="flex flex-col items-center gap-8">
        <h1 className="font-extrabold">Myself</h1>
        <h2> A Visionary builder and tech Enthusiast with expertise in Full Stack Web Development , Machine Learning and DevOps</h2>
      </main>
    </div>
  );
}
