
import streamlit as st

st.set_page_config(
    page_title="StreamWise",
    page_icon="🎓"
)


# 1. School's Grade XI combinations

streams = {
    "Science 1": {
        "compulsory": [
            "English", "Physics", "Chemistry", "Mathematics"
        ],
        "electives": [
            "Computer Science", "Biology", "Economics",
            "Physical Education", "Painting", "Sociology",
            "Informatics Practice", "Psychology", "Legal Studies",
            "Entrepreneurship", "NCC*", "Yoga*",
            "Early Childhood Education*", "French*", "Hindi*",
            "German*", "Artificial Intelligence*", "Bio Technology*",
            "Food Production*"
        ],
        "description": (
            "Includes Physics, Chemistry and Mathematics. "
            "You can also explore electives such as Computer Science, "
            "Biology, Economics, Psychology, etc."
        )
    },

    "Science 2": {
        "compulsory": [
            "English", "Physics", "Chemistry", "Biology"
        ],
        "electives": [
            "Applied Mathematics", "Economics", "Physical Education",
            "Painting", "Sociology", "Informatics Practice",
            "Psychology", "Legal Studies", "Entrepreneurship",
            "NCC*", "Yoga*", "Early Childhood Education*",
            "Hindi*", "German*", "Artificial Intelligence*",
            "French*", "Bio Technology*", "Food Production*"
        ],
        "description": (
            "Includes Physics, Chemistry and Biology. "
            "Electives include Applied Mathematics, Economics, "
            "Psychology and Artificial Intelligence, etc."
        )
    },

    "Commerce 1": {
        "compulsory": [
            "English", "Accountancy", "Business Studies", "Economics"
        ],
        "electives": [
            "Mathematics", "Artificial Intelligence*",
            "Informatics Practice", "Applied Mathematics",
            "Food Production*"
        ],
        "description": (
            "Includes Accountancy, Business Studies and Economics. "
            "Electives include Mathematics, Applied Mathematics "
            "and Informatics Practice, etc."
        )
    },

    "Commerce 2": {
        "compulsory": [
            "English", "Accountancy", "Business Studies", "Economics"
        ],
        "electives": [
            "Physical Education", "Painting", "Sociology",
            "Psychology", "Legal Studies", "Entrepreneurship",
            "NCC*", "Yoga*", "Early Childhood Education*",
            "Hindi*", "German*", "French*", "Food Production*"
        ],
        "description": (
            "Includes Accountancy, Business Studies and Economics. "
            "Electives include Psychology, Sociology, Legal Studies, "
            "Painting and Entrepreneurship, etc."
        )
    },

    "Humanities 1": {
        "compulsory": [
            "English", "History", "Economics", "Political Science"
        ],
        "electives": [
            "Mathematics", "Artificial Intelligence*",
            "Informatics Practice", "Applied Mathematics",
            "Food Production*"
        ],
        "description": (
            "Includes History, Economics and Political Science. "
            "Electives include Mathematics, Applied Mathematics "
            "and Informatics Practice, etc."
        )
    },

    "Humanities 2": {
        "compulsory": [
            "English", "History", "Economics", "Political Science"
        ],
        "electives": [
            "Physical Education", "Painting", "Sociology",
            "Psychology", "Legal Studies", "Entrepreneurship",
            "NCC*", "Yoga*", "Early Childhood Education*",
            "Hindi*", "German*", "French*", "Food Production*"
        ],
        "description": (
            "Includes History, Economics and Political Science. "
            "Electives include Psychology, Sociology, Legal Studies, "
            "Painting and Entrepreneurship, etc."
        )
    }
}


# 2. Welcome page

st.title("StreamWise")
st.subheader("Find a Grade XI combination that fits you.")

st.write(
    "Not sure which combination to choose? Select the subjects "
    "you'd like to continue, compare your options, and explore "
    "the combinations that interest you."
)


# 3. Student introduction

st.header("Let's get to know you")

name = st.text_input("What can I call you?")

if name.strip():

    st.write(f"Hey, {name.strip()}! Let's find your fit.")

    grade = st.radio(
        "Are you in Grade X and choosing subjects for Grade XI?",
        ["Yes", "No"],
        index=None
    )

    if grade == "No":

        st.write(
            "StreamWise is designed for Grade X students "
            "exploring Grade XI combinations."
        )

    elif grade == "Yes":

        # 4. Subject preferences

        st.header("1. What subjects would you like to continue?")

        subject_options = [
            "Mathematics",
            "Biology",
            "Physics",
            "Chemistry",
            "Accountancy",
            "Business Studies",
            "Economics",
            "History",
            "Political Science"
        ]

        wanted_subjects = st.multiselect(
            "Select all the subjects you prefer:",
            subject_options
        )

        if wanted_subjects:

            st.write(
                "**Your preferences:** "
                + ", ".join(wanted_subjects)
            )

            # 5. Compare combinations

            st.header("2. Explore your options")

            st.write(
                "These comparisons show which of your preferred "
                "subjects are compulsory in each combination. "
                "You may also discover options you hadn't considered."
            )

            results = []

            for stream_name, details in streams.items():

                matches = [
                    subject
                    for subject in details["compulsory"]
                    if subject != "English"
                    and subject in wanted_subjects
                ]

                other_subjects = [
                    subject
                    for subject in details["compulsory"]
                    if subject != "English"
                    and subject not in wanted_subjects
                ]

                results.append({
                    "name": stream_name,
                    "details": details,
                    "matches": matches,
                    "other_subjects": other_subjects,
                    "match_count": len(matches)
                })

            # Show more preference matches first.

            results.sort(
                key=lambda result: result["match_count"],
                reverse=True
            )

            for result in results:

                stream_name = result["name"]
                details = result["details"]

                with st.expander(
                    f"{stream_name} "
                    f"({result['match_count']} preference match(es))"
                ):

                    st.write(details["description"])

                    st.write("**Compulsory subjects:**")
                    st.write(", ".join(details["compulsory"]))

                    st.write("**Your preferred subjects included:**")

                    if result["matches"]:
                        st.write(", ".join(result["matches"]))
                    else:
                        st.write(
                            "None of your selected subjects are "
                            "compulsory in this combination."
                        )

                    st.write("**Other compulsory subjects to consider:**")

                    if result["other_subjects"]:
                        st.write(", ".join(result["other_subjects"]))
                    else:
                        st.write(
                            "All non-English compulsory subjects "
                            "are among your preferences."
                        )

            # 6. Select a combination

            st.header("3. Choose a combination to explore")

            chosen_stream = st.selectbox(
                "Which combination interests you?",
                list(streams.keys()),
                index=None,
                placeholder="Choose a combination"
            )

            # Continue only if a combination was selected.

            if chosen_stream is not None:

                chosen_details = streams[chosen_stream]

                st.subheader(chosen_stream)
                st.write(chosen_details["description"])

                st.write("**Compulsory subjects:**")
                st.write(", ".join(chosen_details["compulsory"]))

                # 7. Select one elective

                st.header("4. Choose your elective")

                elective = st.selectbox(
                    "Which elective would you like?",
                    chosen_details["electives"],
                    index=None,
                    placeholder="Choose an elective"
                )

                # Show the final result only after an elective is selected.

                if elective is not None:

                    if elective.endswith("*"):

                        st.warning(
                            "As stated by the school, this elective will "
                            "be offered only if at least 5 students opt for it."
                        )

                    # 8. Final result

                    st.header("Your StreamWise result")

                    st.write(f"**Name:** {name.strip()}")
                    st.write(f"**Combination:** {chosen_stream}")

                    st.write("**Compulsory subjects:**")
                    st.write(", ".join(chosen_details["compulsory"]))

                    st.write(f"**Your elective:** {elective}")

                    st.success(
                        f"Based on your interests, {chosen_stream} "
                        "could be a good match for you!"
                    )

        else:

            st.info(
                "Choose at least one subject to compare "
                "the available combinations."
            )
