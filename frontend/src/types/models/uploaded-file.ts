export type UploadedFile = {
  id: string;
  user_id: string;
  file_name: string;
  file_path: string;
  file_size: number;
  mime_type: string;
  course_id: string;
  created_at: string;
};

const userUuid1 = "a3b8d4e1-7f9b-4c6e-8d2a-5b9c1d0e3f6a";
const userUuid2 = "d9e2c1b0-3a8d-4b5e-9f1c-7e0d2b4a6c9e";
const courseUuid1 = "8f7e6d5c-1a9b-4a3e-bf0d-9c2b5a8e1d4f";
const courseUuid2 = "2c5b8e1d-4f8a-4e6d-a3b8-7f9b4c6e8d2a";

export const dummyFiles = [
  {
    id: "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    user_id: userUuid1,
    file_name: "Lecture Notes Week 1.pdf",
    file_path: `/uploads/${userUuid1}/${courseUuid1}/Lecture_Notes_Week_1.pdf`,
    file_size: 512 * 1024, // 512 KB
    mime_type: "application/pdf",
    course_id: courseUuid1,
    created_at: "2025-04-28T10:30:00Z",
  },
  {
    id: "98a36a1f-e297-4e1a-9a46-8a45c9b27301",
    user_id: userUuid2,
    file_name: "assignment_logo.png",
    file_path: `/uploads/${userUuid2}/${courseUuid2}/assignment_logo.png`,
    file_size: 150 * 1024, // 150 KB
    mime_type: "image/png",
    course_id: courseUuid2,
    created_at: "2025-04-29T14:15:22Z",
  },
  {
    id: "c2a6d0e3-1b9c-4b1f-8c3d-5e8a9b0c2d1e",
    user_id: userUuid1,
    file_name: "Project Proposal Final.docx",
    file_path: `/uploads/${userUuid1}/${courseUuid1}/Project_Proposal_Final.docx`,
    file_size: 78 * 1024, // 78 KB
    mime_type:
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    course_id: courseUuid1,
    created_at: "2025-04-30T09:05:10Z",
  },
  {
    id: "5e8a9b0c-2d1e-4f8c-9a46-1b9c4b1f8c3d",
    user_id: userUuid2,
    file_name: "Introduction Video.mp4",
    file_path: `/uploads/${userUuid2}/${courseUuid2}/Introduction_Video.mp4`,
    file_size: 25 * 1024 * 1024, // 25 MB
    mime_type: "video/mp4",
    course_id: courseUuid2,
    created_at: "2025-05-01T08:00:00Z",
  },
  {
    id: "1b9c4b1f-8c3d-4a9e-b6d1-f47ac10b58cc",
    user_id: userUuid1,
    file_name: "spreadsheet_data.xlsx",
    file_path: `/uploads/${userUuid1}/${courseUuid1}/spreadsheet_data.xlsx`,
    file_size: 320 * 1024, // 320 KB
    mime_type:
      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    course_id: courseUuid1,
    created_at: "2025-05-01T11:45:55Z",
  },
  // --- Added 20 More Items ---
  {
    id: "6a2f9b1e-8d4c-4a7e-bc1d-0e3f6a9b8d5c",
    user_id: userUuid2,
    file_name: "Lab Report 1 Draft.pdf",
    file_path: `/uploads/${userUuid2}/${courseUuid2}/Lab_Report_1_Draft.pdf`,
    file_size: 285 * 1024, // 285 KB
    mime_type: "application/pdf",
    course_id: courseUuid2,
    created_at: "2025-05-02T09:15:00Z",
  },
  {
    id: "b8e3c1d0-5a7f-4b9e-af3c-9e2d4b6a8c1e",
    user_id: userUuid1,
    file_name: "Team Charter v2.docx",
    file_path: `/uploads/${userUuid1}/${courseUuid1}/Team_Charter_v2.docx`,
    file_size: 55 * 1024, // 55 KB
    mime_type:
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    course_id: courseUuid1,
    created_at: "2025-05-02T11:00:30Z",
  },
  {
    id: "e1d4f8a7-9b3e-4c1d-ba5e-3f6a9b8d5c7f",
    user_id: userUuid2,
    file_name: "Reading_Material_Ch3.epub",
    file_path: `/uploads/${userUuid2}/${courseUuid1}/Reading_Material_Ch3.epub`,
    file_size: 1200 * 1024, // 1.2 MB
    mime_type: "application/epub+zip",
    course_id: courseUuid1, // Note: User 2 accessing Course 1 resource
    created_at: "2025-05-03T14:20:30Z",
  },
  {
    id: "3c1d0e3f-6a9b-4d8e-bf7c-5e9a2d4b6a8c",
    user_id: userUuid1,
    file_name: "Midterm Presentation Slides.pptx",
    file_path: `/uploads/${userUuid1}/${courseUuid2}/Midterm_Presentation_Slides.pptx`,
    file_size: 4608 * 1024, // 4.5 MB
    mime_type:
      "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    course_id: courseUuid2,
    created_at: "2025-05-04T16:05:00Z",
  },
  {
    id: "7f9b4c6e-8d2a-4e1d-8f7e-1a9b4a3ebf0d",
    user_id: userUuid2,
    file_name: "helper_utility.py",
    file_path: `/uploads/${userUuid2}/${courseUuid2}/helper_utility.py`,
    file_size: 5 * 1024, // 5 KB
    mime_type: "text/x-python",
    course_id: courseUuid2,
    created_at: "2025-05-05T10:00:15Z",
  },
  {
    id: "4a3ebf0d-9c2b-4f8a-9e2d-6a2f9b1e8d4c",
    user_id: userUuid1,
    file_name: "Research Paper References.bib",
    file_path: `/uploads/${userUuid1}/${courseUuid1}/Research_Paper_References.bib`,
    file_size: 12 * 1024, // 12 KB
    mime_type: "text/x-bibtex",
    course_id: courseUuid1,
    created_at: "2025-05-05T17:30:00Z",
  },
  {
    id: "9e2d4b6a-8c1e-4a7e-bc1d-b8e3c1d05a7f",
    user_id: userUuid2,
    file_name: "Project Architecture Diagram.drawio",
    file_path: `/uploads/${userUuid2}/${courseUuid1}/Project_Architecture_Diagram.drawio`,
    file_size: 95 * 1024, // 95 KB
    mime_type: "application/vnd.jgraph.mxfile", // or application/xml
    course_id: courseUuid1,
    created_at: "2025-05-06T11:22:45Z",
  },
  {
    id: "bc1d0e3f-6a9b-4b9e-af3c-e1d4f8a79b3e",
    user_id: userUuid1,
    file_name: "Optional_Reading_Article.pdf",
    file_path: `/uploads/${userUuid1}/${courseUuid2}/Optional_Reading_Article.pdf`,
    file_size: 850 * 1024, // 850 KB
    mime_type: "application/pdf",
    course_id: courseUuid2,
    created_at: "2025-05-07T08:00:00Z",
  },
  {
    id: "af3c9e2d-4b6a-4c1d-ba5e-3c1d0e3f6a9b",
    user_id: userUuid2,
    file_name: "Survey Results Raw.csv",
    file_path: `/uploads/${userUuid2}/${courseUuid2}/Survey_Results_Raw.csv`,
    file_size: 180 * 1024, // 180 KB
    mime_type: "text/csv",
    course_id: courseUuid2,
    created_at: "2025-05-07T13:10:10Z",
  },
  {
    id: "ba5e3f6a-9b8d-4d8e-bf7c-7f9b4c6e8d2a",
    user_id: userUuid1,
    file_name: "Sample Audio Clip.mp3",
    file_path: `/uploads/${userUuid1}/${courseUuid1}/Sample_Audio_Clip.mp3`,
    file_size: 2 * 1024 * 1024, // 2 MB
    mime_type: "audio/mpeg",
    course_id: courseUuid1,
    created_at: "2025-05-08T10:55:00Z",
  },
  {
    id: "bf7c5e9a-2d4b-4e1d-8f7e-4a3ebf0d9c2b",
    user_id: userUuid2,
    file_name: "Final Project Requirements.txt",
    file_path: `/uploads/${userUuid2}/${courseUuid1}/Final_Project_Requirements.txt`,
    file_size: 3 * 1024, // 3 KB
    mime_type: "text/plain",
    course_id: courseUuid1,
    created_at: "2025-05-08T16:40:00Z",
  },
  {
    id: "8f7e1a9b-4a3e-4f8a-9e2d-9e2d4b6a8c1e",
    user_id: userUuid1,
    file_name: "Code Library Backup.zip",
    file_path: `/uploads/${userUuid1}/backups/Code_Library_Backup.zip`, // Example different path structure
    file_size: 15 * 1024 * 1024, // 15 MB
    mime_type: "application/zip",
    course_id: courseUuid2, // Associated with course 2 maybe
    created_at: "2025-05-09T01:05:00Z",
  },
  {
    id: "9e2d6a2f-9b1e-4a7e-bc1d-bc1d0e3f6a9b",
    user_id: userUuid2,
    file_name: "Marketing Image Banner.jpg",
    file_path: `/uploads/${userUuid2}/${courseUuid2}/Marketing_Image_Banner.jpg`,
    file_size: 450 * 1024, // 450 KB
    mime_type: "image/jpeg",
    course_id: courseUuid2,
    created_at: "2025-05-09T11:11:11Z",
  },
  {
    id: "bc1db8e3-c1d0-4b9e-af3c-af3c9e2d4b6a",
    user_id: userUuid1,
    file_name: "Lecture_Wk5_Transcript.txt",
    file_path: `/uploads/${userUuid1}/${courseUuid1}/Lecture_Wk5_Transcript.txt`,
    file_size: 45 * 1024, // 45 KB
    mime_type: "text/plain",
    course_id: courseUuid1,
    created_at: "2025-05-10T09:00:00Z",
  },
  {
    id: "af3ce1d4-f8a7-4c1d-ba5e-ba5e3f6a9b8d",
    user_id: userUuid2,
    file_name: "User Manual Draft.pdf",
    file_path: `/uploads/${userUuid2}/${courseUuid1}/User_Manual_Draft.pdf`,
    file_size: 980 * 1024, // 980 KB
    mime_type: "application/pdf",
    course_id: courseUuid1,
    created_at: "2025-05-10T15:30:45Z",
  },
  {
    id: "ba5e3c1d-0e3f-4d8e-bf7c-bf7c5e9a2d4b",
    user_id: userUuid1,
    file_name: "Configuration File.json",
    file_path: `/uploads/${userUuid1}/${courseUuid2}/Configuration_File.json`,
    file_size: 2 * 1024, // 2 KB
    mime_type: "application/json",
    course_id: courseUuid2,
    created_at: "2025-05-11T12:00:00Z",
  },
  {
    id: "bf7c7f9b-4c6e-4e1d-8f7e-8f7e1a9b4a3e",
    user_id: userUuid2,
    file_name: "Team Photo 2025.jpg",
    file_path: `/uploads/${userUuid2}/general/Team_Photo_2025.jpg`, // Another path example
    file_size: 3 * 1024 * 1024, // 3 MB
    mime_type: "image/jpeg",
    course_id: courseUuid1, // Maybe related to course 1 team
    created_at: "2025-05-11T18:15:00Z",
  },
  {
    id: "8f7e4a3e-bf0d-4f8a-9e2d-9e2d6a2f9b1e",
    user_id: userUuid1,
    file_name: "Final Report - Appendix.docx",
    file_path: `/uploads/${userUuid1}/${courseUuid1}/Final_Report_Appendix.docx`,
    file_size: 150 * 1024, // 150 KB
    mime_type:
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    course_id: courseUuid1,
    created_at: "2025-05-12T09:30:00Z",
  },
  {
    id: "9e2d9e2d-4b6a-4a7e-bc1d-bc1db8e3c1d0",
    user_id: userUuid2,
    file_name: "Animated Logo.gif",
    file_path: `/uploads/${userUuid2}/${courseUuid2}/Animated_Logo.gif`,
    file_size: 750 * 1024, // 750 KB
    mime_type: "image/gif",
    course_id: courseUuid2,
    created_at: "2025-05-12T14:00:00Z",
  },
  {
    id: "bc1daf3c-9e2d-4b9e-af3c-af3ce1d4f8a7",
    user_id: userUuid1,
    file_name: "License Agreement.pdf",
    file_path: `/uploads/${userUuid1}/legal/License_Agreement.pdf`, // Yet another path
    file_size: 110 * 1024, // 110 KB
    mime_type: "application/pdf",
    course_id: courseUuid1, // Associated with course 1?
    created_at: "2025-05-13T10:00:00Z",
  },
];
