import Link from 'next/link';

export default function Navbar(){
    return(
        <nav className="">
            <div className="flex justify-center font-bold gap-8 p-4 text-amber-600">
                <Link href="/">Home</Link>
                <Link href="/about">About</Link>
                <Link href="/projects">Projects</Link>
                <Link href="/contact">Contact</Link>
            </div>
        </nav>
    )
}