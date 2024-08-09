def get_response(user_input: str) -> str:
    if user_input == "!pull":
        return "Deadlifts 1x5\nPullups 3x Max\nSmith Machine Rows 3x8-12\nFace Pulls 3x15-20\nHammer Curls 3x8-12\nBicep Curls 3x8-12"
    elif user_input == "!push":
        return "Bench Press 3x5\nOverhead Press 3x5\nIncline Bench Press 3x8-12\nSkull crushers 3x12 Superset with Lateral Raises 3x15-20\nTricep pushdowns 3x8-12 Superset with Lateral Raises 3x15-20"
    elif user_input == "!leg":
        return "Remember to warmup properly\nTib Raises 15 lbs 3x15-20 Superset with seated calf raises\nSquats 3x5\Bulgarian split squats 3x8-12\nDumbbell RDLs 3x8-12\nLying Leg Curls 3x8-12"
    