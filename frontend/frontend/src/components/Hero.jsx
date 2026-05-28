import { Link } from "react-router-dom";

function Hero() {
  return (
    <section className="min-h-[85vh] flex flex-col items-center justify-center text-center px-6">
      <h1 className="text-6xl font-bold text-gray-900 max-w-5xl leading-tight">
        AI-Powered Placement Outreach Automation
      </h1>

      <p className="mt-6 text-xl text-gray-600 max-w-3xl">
        Extract hiring companies from job portals, discover recruiter emails,
        and generate personalized placement invitation emails using AI.
      </p>

      <div className="mt-10 flex gap-5">
        <Link
          to="/dashboard"
          className="bg-blue-600 text-white px-8 py-4 rounded-2xl text-lg hover:bg-blue-700 transition shadow-md"
        >
          Start Using
        </Link>

        <Link
          to="/setup"
          className="bg-white border border-gray-300 px-8 py-4 rounded-2xl text-lg hover:bg-gray-100 transition"
        >
          Setup Guide
        </Link>
      </div>
    </section>
  );
}

export default Hero;