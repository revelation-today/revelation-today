---
Title: "Contact Us"
---

{{< formkeep_extended exampletoken >}}
  <input type="text" name="Name" placeholder="Your Name">
  <input type="text" name="WhatsApp" placeholder="0177 999 999 99">
  <input type="text" name="Feedback" placeholder="Your Feedback">
{{</ formkeep_extended >}}

<div class="w-full md:w-96 md:max-w-full mx-auto">
  <div class="p-6 border border-gray-600 sm:rounded-md bg-gray-800">
<form method="POST" action="https://herotofu.com/f38992e0-2bb1-11ef-bb50-597c09297146">
      <label class="block mb-6">
        <span class="text-gray-300">Your name</span>
        <input
          name="name"
          type="text"
          class="
            block
            w-full
            mt-1
            border-gray-600
            rounded-md
            shadow-sm
            focus:border-indigo-300
            focus:ring
            focus:ring-indigo-200
            focus:ring-opacity-50
            bg-transparent
            placeholder-gray-600
            text-gray-300
          "
          placeholder="Joe Bloggs"
        />
    </label>
      <label class="block mb-6">
        <span class="text-gray-300">Email address</span>
        <input
          name="email"
          type="email"
          class="
            block
            w-full
            mt-1
            border-gray-600
            rounded-md
            shadow-sm
            focus:border-indigo-300
            focus:ring
            focus:ring-indigo-200
            focus:ring-opacity-50
            bg-transparent
            placeholder-gray-600
            text-gray-300
          "
placeholder="joe.bloggs@example.com"
          required
        />
      </label>
      <label class="block mb-6">
        <span class="text-gray-300">Message</span>
        <textarea
          name="message"
        name="message"
          class="
            block
            w-full
            mt-1
            border-gray-600
            rounded-md
            shadow-sm
            focus:border-indigo-300
            focus:ring
            focus:ring-indigo-200
            focus:ring-opacity-50
            bg-transparent
            placeholder-gray-600
            text-gray-300
          "
          rows="3"
  placeholder="Tell us what you're thinking about..."
        ></textarea>
      </label>
      <div class="mb-6">
        <button
          type="submit"
          class="
            h-10
            px-5
            text-indigo-100
            bg-indigo-700
            rounded-lg
            transition-colors
            duration-150
            focus:shadow-outline
            hover:bg-indigo-800
          "
        >
          Contact Us
        </button>
      </div>
      <div>